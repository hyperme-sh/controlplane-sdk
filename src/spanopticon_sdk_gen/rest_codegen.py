"""Invoke openapi-generator (Docker) for REST client SDKs."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Sequence
from copy import deepcopy
from pathlib import Path
from typing import Any

from spanopticon_sdk_gen.json_dates import install_json_dates
from spanopticon_sdk_gen.rest_contract import (
    install_usage_compatibility,
    map_codegen_tags,
    validate_generated_operations,
)

DEFAULT_IMAGE = "openapitools/openapi-generator-cli@sha256:f2054a5a7908ad81017d0f0839514ba5eab06ae628914ff71554d46fac1bcf7a"
CODEGEN_SPEC_REL = Path(".cache/sdk-gen/openapi.codegen.json")


def _is_null_schema(schema: Any) -> bool:
    return isinstance(schema, dict) and schema.get("type") == "null"


def sanitize_openapi_for_generator(doc: dict[str, Any]) -> dict[str, Any]:
    """Rewrite OAS 3.1 null unions so openapi-generator (esp. Python) can emit models.

    FastAPI emits ``anyOf: [T, {type: null}]``. Generator 7.10+ still crashes on
    those as ``any_of_1`` / ``openApiType=null``. Convert to ``nullable: true``.
    """

    def rewrite(obj: Any) -> Any:
        if isinstance(obj, list):
            return [rewrite(x) for x in obj]
        if not isinstance(obj, dict):
            return obj
        obj = {k: rewrite(v) for k, v in obj.items()}
        anyof = obj.get("anyOf")
        if isinstance(anyof, list):
            nulls = [x for x in anyof if _is_null_schema(x)]
            others = [x for x in anyof if not _is_null_schema(x)]
            if nulls and others:
                extras = {k: v for k, v in obj.items() if k != "anyOf"}
                extras["nullable"] = True
                if len(others) == 1 and isinstance(others[0], dict):
                    other = others[0]
                    if "$ref" in other:
                        merged = dict(extras)
                        merged["allOf"] = [{"$ref": other["$ref"]}]
                        for key in ("description", "title"):
                            if key in other:
                                merged.setdefault(key, other[key])
                        return merged
                    return {**other, **extras}
                extras["anyOf"] = others
                return extras
        t = obj.get("type")
        if isinstance(t, list) and "null" in t:
            non_null = [x for x in t if x != "null"]
            if len(non_null) == 1:
                obj["type"] = non_null[0]
            elif non_null:
                obj["type"] = non_null
            else:
                obj.pop("type", None)
            obj["nullable"] = True
        return obj

    return map_codegen_tags(rewrite(deepcopy(doc)))


def write_codegen_openapi(repo_root: Path, spec_rel: Path) -> Path:
    """Write a generator-safe copy of the committed spec (not for console/SDK source)."""
    src = repo_root / spec_rel
    raw = json.loads(src.read_text(encoding="utf-8"))
    out = repo_root / CODEGEN_SPEC_REL
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(sanitize_openapi_for_generator(raw), indent=2) + "\n",
        encoding="utf-8",
    )
    return CODEGEN_SPEC_REL


def _repo_mount_args(repo_root: Path) -> list[str]:
    return ["-v", f"{repo_root.resolve()}:/local"]


def run_openapi_generator_docker(
    *,
    repo_root: Path,
    spec_container_path: str,
    generator: str,
    output_container_path: str,
    additional_properties: Sequence[str] | None = None,
    docker_bin: str = "docker",
    image: str = DEFAULT_IMAGE,
    extra_args: Sequence[str] | None = None,
) -> None:
    """Run ``openapi-generator-cli generate`` inside Docker.

    Paths are under ``/local`` inside the container (repo mounted at ``/local``).
    """
    cmd: list[str] = [
        docker_bin,
        "run",
        "--rm",
        # Use only local image; run_all.sh pulls explicitly (avoids duplicate registry hits).
        "--pull=never",
        "--user",
        f"{os.getuid()}:{os.getgid()}",
        *_repo_mount_args(repo_root),
        image,
        "generate",
        "-i",
        spec_container_path,
        "-g",
        generator,
        "-o",
        output_container_path,
        "--skip-validate-spec",
    ]
    if additional_properties:
        cmd.append(f"--additional-properties={','.join(additional_properties)}")
    if extra_args:
        cmd.extend(extra_args)
    subprocess.check_call(cmd, cwd=repo_root, env={**os.environ})


REST_PRESETS: dict[str, tuple[str, list[str]]] = {
    "typescript-fetch": (
        "typescript-fetch",
        [
            "supportsES6=true",
            "typescriptThreePlus=true",
            "withInterfaces=true",
        ],
    ),
    "python": (
        "python",
        [
            "library=urllib3",
            "recursionLimit=200",
        ],
    ),
    "kotlin": (
        "kotlin",
        [
            "library=jvm-retrofit2",
            "serializationLibrary=jackson",
            "useCoroutines=true",
        ],
    ),
    "swift5": (
        "swift5",
        [
            "responseAs=AsyncAwait",
            "objcCompatible=false",
            "readonlyProperties=true",
        ],
    ),
}


def generate_rest_language(
    *,
    repo_root: Path,
    spec_rel: Path,
    out_rel: Path,
    language_key: str,
    docker_bin: str = "docker",
    image: str = DEFAULT_IMAGE,
) -> None:
    if language_key not in REST_PRESETS:
        raise ValueError(
            f"unknown language {language_key!r}; choose from {sorted(REST_PRESETS)}"
        )
    gen, props = REST_PRESETS[language_key]
    props = [*props, "hideGenerationTimestamp=true"]
    spec_in = "/local/" + spec_rel.as_posix()
    # Validate a clean generation before replacing any committed artifacts.
    cache = repo_root / ".cache/sdk-gen"
    cache.mkdir(parents=True, exist_ok=True)
    document = json.loads((repo_root / spec_rel).read_text())
    with tempfile.TemporaryDirectory(prefix="rest-", dir=cache) as directory:
        stage = Path(directory)
        run_openapi_generator_docker(
            repo_root=repo_root,
            spec_container_path=spec_in,
            generator=gen,
            output_container_path="/local/" + stage.relative_to(repo_root).as_posix(),
            additional_properties=props,
            docker_bin=docker_bin,
            image=image,
        )
        validate_generated_operations(stage, language_key, document)
        aliases = install_usage_compatibility(stage, language_key)
        if language_key == "python":
            aliases += install_json_dates(stage)
        manifest = stage / ".openapi-generator/FILES"
        generated = (
            set(manifest.read_text().splitlines())
            | set(aliases)
            | {".openapi-generator/FILES", ".openapi-generator/VERSION"}
        )
        for name in generated:
            if Path(name).is_absolute() or ".." in Path(name).parts:
                raise ValueError("Generator manifest contains an unsafe path")
        manifest.write_text(
            "\n".join(
                sorted(
                    generated
                    - {".openapi-generator/FILES", ".openapi-generator/VERSION"}
                )
            )
            + "\n"
        )
        output = repo_root / out_rel
        old_manifest = output / ".openapi-generator/FILES"
        old = (
            set(old_manifest.read_text().splitlines())
            if old_manifest.exists()
            else set()
        )
        for name in old - generated:
            relative = Path(name)
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError("Existing generator manifest contains an unsafe path")
            target = output / relative
            if target.is_file():
                target.unlink()
        for source in stage.rglob("*"):
            if source.is_file():
                target = output / source.relative_to(stage)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)


def main_preset_list() -> None:
    print(" ".join(sorted(REST_PRESETS.keys())))


if __name__ == "__main__":
    main_preset_list()
    sys.exit(0)

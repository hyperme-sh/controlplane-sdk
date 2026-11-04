#!/usr/bin/env python3
"""Generate REST clients (TypeScript, Python, Kotlin, Swift) via openapi-generator Docker."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO / "scripts" / "sdk-gen") not in sys.path:
    sys.path.insert(0, str(_REPO / "scripts" / "sdk-gen"))

from panopticon_sdk_gen.rest_codegen import (  # noqa: E402
    REST_PRESETS,
    generate_rest_language,
    write_codegen_openapi,
)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--spec",
        type=Path,
        default=_REPO / "sdk" / "openapi" / "v1" / "openapi.json",
        help="OpenAPI spec path under repo",
    )
    p.add_argument(
        "--out-root",
        type=Path,
        default=_REPO / "sdk" / "rest",
        help="Output root (language dirs created underneath)",
    )
    p.add_argument(
        "--lang",
        action="append",
        dest="langs",
        choices=sorted(REST_PRESETS.keys()),
        help="Language preset (repeat for multiple); default: all",
    )
    p.add_argument("--docker", default="docker", help="Docker CLI binary")
    p.add_argument(
        "--image",
        default=os.environ.get(
            "OPENAPI_GENERATOR_IMAGE", "openapitools/openapi-generator-cli:v7.10.0"
        ),
        help="openapi-generator image (or set OPENAPI_GENERATOR_IMAGE)",
    )
    args = p.parse_args()

    spec_rel = args.spec.resolve().relative_to(_REPO.resolve())
    langs = args.langs or sorted(REST_PRESETS.keys())
    spec_rel = write_codegen_openapi(_REPO, spec_rel)

    for key in langs:
        out_rel = (args.out_root / key).resolve().relative_to(_REPO.resolve())
        generate_rest_language(
            repo_root=_REPO,
            spec_rel=spec_rel,
            out_rel=out_rel,
            language_key=key,
            docker_bin=args.docker,
            image=args.image,
        )
        print(f"Generated REST SDK: {key} -> {args.out_root / key}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

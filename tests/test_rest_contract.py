"""Every committed client must retain every canonical method/path, including AI usage."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
from spanopticon_sdk_gen.rest_codegen import sanitize_openapi_for_generator
from spanopticon_sdk_gen.rest_contract import (
    emitted_operations,
    install_usage_compatibility,
    validate_generated_operations,
)


@pytest.mark.parametrize("language", ["python", "typescript-fetch", "kotlin", "swift5"])
def test_committed_client_retains_every_operation(language):
    document = json.loads((ROOT / "sdk/openapi/v1/openapi.json").read_text())
    directory = ROOT / "sdk/rest" / language
    validate_generated_operations(directory, language, document)
    # An operation without an operationId must still be checked.
    document["paths"]["/api/v1/ai/usage/history"]["post"] = {"tags": ["ai"]}
    with pytest.raises(ValueError, match="operation coverage mismatch"):
        validate_generated_operations(directory, language, document)


def test_tag_mapping_changes_only_generator_copy():
    document = {
        "paths": {
            "/inference": {"post": {"tags": ["AI"]}},
            "/usage": {"get": {"tags": ["ai"]}},
        },
        "tags": [{"name": "ai"}, {"name": "AI"}],
        "components": {
            "schemas": {"Record": {"properties": {"tags": {"default": ["ai"]}}}}
        },
    }
    before = deepcopy(document)
    generated = sanitize_openapi_for_generator(document)
    assert document == before
    assert generated["paths"]["/usage"]["get"]["tags"] == ["AIUsage"]
    assert generated["paths"]["/inference"]["post"]["tags"] == ["AI"]
    assert generated["tags"] == [{"name": "AIUsage"}, {"name": "AI"}]
    assert generated["components"] == document["components"]


def test_unknown_case_collision_fails_instead_of_overwriting():
    document = {
        "paths": {
            "/a": {"get": {"tags": ["Other"]}},
            "/b": {"get": {"tags": ["other"]}},
        }
    }
    with pytest.raises(ValueError, match="explicit mapping"):
        sanitize_openapi_for_generator(document)


@pytest.mark.parametrize("language", ["python", "typescript-fetch", "kotlin", "swift5"])
def test_no_usage_alias_for_specs_without_usage(tmp_path, language):
    assert install_usage_compatibility(tmp_path, language) == []


@pytest.mark.parametrize("declaration", ["let", "var"])
def test_swift_path_parameters_are_inventoried(tmp_path, declaration):
    directory = tmp_path / "OpenAPIClient/Classes/OpenAPIs/APIs"
    directory.mkdir(parents=True)
    (directory / "Example.swift").write_text(
        f'{declaration} localVariablePath = "/items/{{id}}"\n'
        'return builder.init(method: "DELETE", URLString: localVariablePath)\n'
    )
    assert emitted_operations(tmp_path, "swift5") == {("DELETE", "/items/{id}")}


def test_failed_generation_keeps_existing_client(tmp_path, monkeypatch):
    from spanopticon_sdk_gen import rest_codegen

    spec = tmp_path / "spec.json"
    spec.write_text(json.dumps({"paths": {"/required": {"get": {}}}}))
    output = tmp_path / "output"
    output.mkdir()
    original = output / "keep.py"
    original.write_text("original")
    monkeypatch.setattr(
        rest_codegen, "run_openapi_generator_docker", lambda **kwargs: None
    )
    with pytest.raises(ValueError, match="operation coverage mismatch"):
        rest_codegen.generate_rest_language(
            repo_root=tmp_path,
            spec_rel=Path("spec.json"),
            out_rel=Path("output"),
            language_key="python",
        )
    assert original.read_text() == "original"


def test_successful_generation_removes_only_obsolete_managed_files(
    tmp_path, monkeypatch
):
    from spanopticon_sdk_gen import rest_codegen

    (tmp_path / "spec.json").write_text(json.dumps({"paths": {}}))
    output = tmp_path / "output"
    (output / ".openapi-generator").mkdir(parents=True)
    (output / ".openapi-generator/FILES").write_text("obsolete.py\n")
    (output / "obsolete.py").write_text("obsolete")
    (output / "custom.py").write_text("custom")

    def generate(**kwargs):
        stage = tmp_path / kwargs["output_container_path"].removeprefix("/local/")
        (stage / "openapi_client/api").mkdir(parents=True)
        (stage / ".openapi-generator").mkdir()
        (stage / ".openapi-generator/FILES").write_text("new.py\n")
        (stage / ".openapi-generator/VERSION").write_text("7.10.0")
        (stage / "new.py").write_text("new")

    monkeypatch.setattr(rest_codegen, "run_openapi_generator_docker", generate)
    rest_codegen.generate_rest_language(
        repo_root=tmp_path,
        spec_rel=Path("spec.json"),
        out_rel=Path("output"),
        language_key="python",
    )
    assert not (output / "obsolete.py").exists()
    assert (output / "custom.py").read_text() == "custom"
    assert (output / "new.py").read_text() == "new"

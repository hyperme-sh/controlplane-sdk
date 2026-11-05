"""Real installed-edge offline export, transferred from the monorepo."""
import json
from pathlib import Path
import pytest
import respx
from spanopticon_sdk_gen.export import build_merged_openapi_offline, run_export_offline_sync
from spanopticon_sdk_gen.breaking import is_breaking_change

@pytest.fixture(autouse=True)
def isolated_offline_owner_environment(monkeypatch, tmp_path):
    from controlplane_edge.aggregation_settings import OpenAPIAggregationSettings

    monkeypatch.chdir(tmp_path)
    for field in OpenAPIAggregationSettings.model_fields.values():
        aliases = field.validation_alias
        for name in getattr(aliases, "choices", [aliases]):
            if isinstance(name, str):
                monkeypatch.delenv(name, raising=False)
    # Real edge composition; any unexpected upstream HTTP request fails locally.
    with respx.mock(assert_all_called=False):
        yield


@pytest.mark.asyncio
async def test_offline_export_includes_openapi_key():
    doc = await build_merged_openapi_offline(version_label="v1")
    assert "openapi" in doc
    assert "paths" in doc

def test_offline_export_sync_keeps_committed_spec(tmp_path: Path):
    existing = {
        "openapi": "3.1.0",
        "info": {"title": "Panopticon Control Plane API", "version": "1.0.0"},
        "paths": {
            "/api/v1/account/me": {"get": {"responses": {"200": {"description": "ok"}}}},
            "/api/v1/acl/enforce": {"post": {"responses": {"200": {"description": "ok"}}}},
        },
        "components": {"schemas": {"AuthMeResponse": {"type": "object"}}},
    }
    out = tmp_path / "openapi.json"
    raw = json.dumps(existing, indent=2) + "\n"
    out.write_text(raw, encoding="utf-8")
    run_export_offline_sync(out)
    assert out.read_text(encoding="utf-8") == raw
    breaking, _d = is_breaking_change(existing, json.loads(out.read_text(encoding="utf-8")))
    assert breaking is False

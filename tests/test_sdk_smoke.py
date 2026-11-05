"""The committed SDK OpenAPI document is required, not optional coverage."""
import json
from pathlib import Path

def test_sdk_openapi_json_is_openapi_document():
    spec = Path(__file__).resolve().parents[1] / "sdk/openapi/v1/openapi.json"
    data = json.loads(spec.read_text(encoding="utf-8"))
    assert "openapi" in data
    assert "paths" in data
    assert "info" in data

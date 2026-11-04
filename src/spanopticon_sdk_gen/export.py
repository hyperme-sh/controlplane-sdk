"""Fetch or build merged gateway OpenAPI (per API version label)."""

from __future__ import annotations

import asyncio
import json
import logging
import time
from copy import deepcopy
from pathlib import Path
from typing import Any

import httpx

logger = logging.getLogger(__name__)

# Stub-only path from build_merged_openapi_offline when remotes are unset.
_OFFLINE_STUB_PATHS = frozenset({"/export-health"})


async def build_merged_openapi_offline(
    *,
    version_label: str = "v1",
) -> dict[str, Any]:
    """Build merged OpenAPI without calling upstream services (monolith + empty remotes).

    Requires ``gateway`` on ``PYTHONPATH`` (same as ``uv run --project controlplane-edge``).
    """
    from fastapi import FastAPI

    from controlplane_edge.aggregation_settings import OpenAPIAggregationSettings
    from controlplane_edge.openapi_aggregate import build_merged_openapi_for_version

    app = FastAPI(title="spanopticon Gateway (export)", version="1.0.0")

    @app.get("/export-health")
    def _health():
        return {"ok": True}

    settings = OpenAPIAggregationSettings()
    return await build_merged_openapi_for_version(app, settings, version_label=version_label)


def fetch_openapi_with_retry(
    url: str,
    *,
    max_retries: int = 4,
    initial_backoff_s: float = 0.5,
    timeout_s: float = 60.0,
) -> dict[str, Any]:
    """GET JSON OpenAPI document with exponential backoff on 5xx/connection errors."""

    last_exc: Exception | None = None
    backoff = initial_backoff_s
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=httpx.Timeout(timeout_s)) as client:
                r = client.get(url)
                r.raise_for_status()
                return r.json()
        except (httpx.HTTPError, ValueError) as e:
            last_exc = e
            logger.warning("fetch attempt %s/%s failed: %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                time.sleep(backoff)
                backoff *= 2
    assert last_exc is not None
    raise last_exc


def write_openapi_json(path: Path, doc: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_openapi_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _path_keys(doc: dict[str, Any]) -> set[str]:
    return set((doc.get("paths") or {}).keys())


def _schema_keys(doc: dict[str, Any]) -> set[str]:
    return set((doc.get("components") or {}).get("schemas", {}).keys())


def offline_export_is_incomplete(generated: dict[str, Any], existing: dict[str, Any]) -> bool:
    """True when offline output dropped committed remotes (no upstreams configured)."""
    exist_paths = _path_keys(existing)
    gen_paths = _path_keys(generated) - _OFFLINE_STUB_PATHS
    if not exist_paths:
        return False
    return not exist_paths.issubset(gen_paths)


def merge_offline_with_existing(
    existing: dict[str, Any],
    generated: dict[str, Any],
) -> dict[str, Any]:
    """Keep committed paths/schemas; add any new non-stub keys from the offline build."""
    out = deepcopy(existing)
    out.setdefault("paths", {})
    for path, item in (generated.get("paths") or {}).items():
        if path in _OFFLINE_STUB_PATHS:
            continue
        if path not in out["paths"]:
            out["paths"][path] = deepcopy(item)
    gen_schemas = (generated.get("components") or {}).get("schemas") or {}
    out_schemas = out.setdefault("components", {}).setdefault("schemas", {})
    for name, schema in gen_schemas.items():
        if name not in out_schemas:
            out_schemas[name] = deepcopy(schema)
    return out


def run_export_offline_sync(
    out: Path,
    *,
    version_label: str = "v1",
) -> None:
    generated = asyncio.run(build_merged_openapi_offline(version_label=version_label))
    if out.is_file():
        existing = load_openapi_json(out)
        if offline_export_is_incomplete(generated, existing):
            merged = merge_offline_with_existing(existing, generated)
            if _path_keys(merged) == _path_keys(existing) and _schema_keys(merged) == _schema_keys(
                existing
            ):
                logger.info(
                    "Offline export has no remotes; keeping committed spec at %s (%s paths)",
                    out,
                    len(_path_keys(existing)),
                )
                return
            logger.info(
                "Offline export missing remotes; preserved committed paths and added %s new path(s)",
                len(_path_keys(merged) - _path_keys(existing)),
            )
            write_openapi_json(out, merged)
            return
    write_openapi_json(out, generated)


def run_export_url_sync(
    base_url: str,
    out: Path,
    *,
    version: str = "v1",
    max_retries: int = 4,
) -> None:
    base = base_url.rstrip("/")
    url = f"{base}/{version}/openapi.json"
    doc = fetch_openapi_with_retry(url, max_retries=max_retries)
    write_openapi_json(out, doc)

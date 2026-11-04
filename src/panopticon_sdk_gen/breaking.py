"""Detect breaking OpenAPI changes (removed paths or component schemas)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def diff_openapi_structure(
    a: dict[str, Any],
    b: dict[str, Any],
) -> dict[str, Any]:
    """Same shape as :func:`gateway.openapi_merge.diff_openapi_changelog`."""

    paths_a = set((a.get("paths") or {}).keys())
    paths_b = set((b.get("paths") or {}).keys())
    schemas_a = set((a.get("components") or {}).get("schemas", {}).keys())
    schemas_b = set((b.get("components") or {}).get("schemas", {}).keys())
    return {
        "paths_added": sorted(paths_b - paths_a),
        "paths_removed": sorted(paths_a - paths_b),
        "schemas_added": sorted(schemas_b - schemas_a),
        "schemas_removed": sorted(schemas_a - schemas_b),
        "info_changed": (a.get("info") or {}) != (b.get("info") or {}),
    }


def load_allowed_removals(path: Path) -> dict[str, set[str]]:
    """Paths and schemas a reviewed change removes on purpose.

    The file is JSON: ``{"paths": [...], "schemas": [...]}``. A missing file
    allows nothing.
    """

    if not path.is_file():
        return {"paths": set(), "schemas": set()}
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("allowed removals must be a JSON object")
    allowed: dict[str, set[str]] = {}
    for key in ("paths", "schemas"):
        values = raw.get(key, [])
        if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
            raise ValueError(f"allowed removals {key} must be a list of strings")
        allowed[key] = set(values)
    return allowed


def is_breaking_change(
    old: dict[str, Any],
    new: dict[str, Any],
    allowed: dict[str, set[str]] | None = None,
) -> tuple[bool, dict[str, Any]]:
    """Breaking if any path or component schema was removed.

    Removals listed in ``allowed`` are reported but do not count as breaking.
    """

    d = diff_openapi_structure(old, new)
    allowed = allowed or {}
    paths = [p for p in d["paths_removed"] if p not in allowed.get("paths", set())]
    schemas = [s for s in d["schemas_removed"] if s not in allowed.get("schemas", set())]
    d["paths_removed_allowed"] = sorted(set(d["paths_removed"]) - set(paths))
    d["schemas_removed_allowed"] = sorted(set(d["schemas_removed"]) - set(schemas))
    d["paths_removed"] = paths
    d["schemas_removed"] = schemas
    breaking = bool(paths or schemas)
    return breaking, d


def describe_breaking(d: dict[str, Any]) -> str:
    lines = []
    if d["paths_removed"]:
        lines.append("paths_removed: " + ", ".join(d["paths_removed"][:20]))
        if len(d["paths_removed"]) > 20:
            lines.append(f"... and {len(d['paths_removed']) - 20} more paths")
    if d["schemas_removed"]:
        lines.append("schemas_removed: " + ", ".join(d["schemas_removed"][:20]))
        if len(d["schemas_removed"]) > 20:
            lines.append(f"... and {len(d['schemas_removed']) - 20} more schemas")
    return "\n".join(lines) or "no removals"

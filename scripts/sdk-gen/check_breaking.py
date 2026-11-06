#!/usr/bin/env python3
"""Fail if the new OpenAPI removes paths or schemas vs a baseline (breaking SDK change)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO / "scripts" / "sdk-gen") not in sys.path:
    sys.path.insert(0, str(_REPO / "scripts" / "sdk-gen"))

from spanopticon_sdk_gen.breaking import (  # noqa: E402
    describe_breaking,
    is_breaking_change,
    load_allowed_removals,
)
from spanopticon_sdk_gen.export import load_openapi_json  # noqa: E402


def _git_show(path_in_repo: str) -> dict | None:
    try:
        raw = subprocess.check_output(
            ["git", "-C", str(_REPO), "show", f"HEAD:{path_in_repo}"],
            stderr=subprocess.DEVNULL,
        )
        return json.loads(raw.decode("utf-8"))
    except (subprocess.CalledProcessError, json.JSONDecodeError, OSError):
        return None


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--new", type=Path, required=True, help="New OpenAPI JSON path")
    p.add_argument(
        "--baseline-file",
        type=Path,
        help="Previous spec JSON file (overrides --git-path)",
    )
    p.add_argument(
        "--git-path",
        default="sdk/openapi/v1/openapi.json",
        help="Path in last commit to compare (default: sdk/openapi/v1/openapi.json)",
    )
    p.add_argument(
        "--allowed-removals",
        type=Path,
        default=_REPO / "scripts" / "sdk-gen" / "allowed-removals.json",
        help="JSON file listing paths and schemas removed on purpose",
    )
    p.add_argument(
        "--allow-missing-baseline",
        action="store_true",
        help="Exit 0 when baseline is missing (first SDK commit)",
    )
    args = p.parse_args()

    new_doc = load_openapi_json(args.new)

    old_doc: dict | None = None
    if args.baseline_file and args.baseline_file.is_file():
        old_doc = load_openapi_json(args.baseline_file)
    elif args.baseline_file and not args.baseline_file.is_file():
        print("baseline file not found:", args.baseline_file, file=sys.stderr)
        return 2
    else:
        old_doc = _git_show(args.git_path)

    if old_doc is None:
        if args.allow_missing_baseline:
            print("No baseline OpenAPI; explicit bootstrap only, compatibility was not checked.")
            return 0
        print("No baseline OpenAPI; compatibility cannot be established. Supply --baseline-file or explicitly bootstrap with --allow-missing-baseline.", file=sys.stderr)
        return 2

    breaking, detail = is_breaking_change(
        old_doc, new_doc, load_allowed_removals(args.allowed_removals)
    )
    allowed = detail["paths_removed_allowed"] + detail["schemas_removed_allowed"]
    if allowed:
        print("Removed on purpose (allowed-removals): " + ", ".join(allowed))
    if breaking:
        print("BREAKING OpenAPI change (removed paths or schemas):", file=sys.stderr)
        print(describe_breaking(detail), file=sys.stderr)
        return 1

    print("OK: no unlisted path/schema removals vs baseline.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

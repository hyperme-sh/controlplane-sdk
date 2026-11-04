#!/usr/bin/env python3
"""Audit tracked organization source against canonical naming and reviewed exceptions."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("repos_root", type=Path, help="Directory containing all organization checkouts")
args = parser.parse_args()
manifest = json.loads((Path(__file__).resolve().parents[1] / "docs/naming-exceptions.json").read_text())
allowed = {(e["repo"], e["path"], e["line_sha256"]) for e in manifest["exceptions"]}
canonical = "spanopticon"
legacy = re.compile(r"(?<![sS)])" + canonical[1:], re.IGNORECASE)
seen = set()
failures = []
for name in manifest["repositories"]:
    repo = args.repos_root / name
    if not (repo / ".git").exists():
        failures.append(f"Missing checkout: {name}")
        continue
    files = subprocess.check_output(["git", "ls-files", "-z"], cwd=repo).decode().split("\0")
    for relative in filter(None, files):
        path = repo / relative
        if not path.exists():
            failures.append(f"Missing tracked file: {name}/{relative}")
            continue
        if legacy.search(relative):
            failures.append(f"Legacy path: {name}/{relative}")
        try:
            lines = path.read_text().splitlines()
        except UnicodeError:
            continue
        for number, line in enumerate(lines, 1):
            if not legacy.search(line):
                continue
            key = (name, relative, hashlib.sha256(line.encode()).hexdigest())
            if key in allowed:
                seen.add(key)
            else:
                failures.append(f"Unreviewed legacy reference: {name}/{relative}:{number}")
for name, path, _ in allowed - seen:
    failures.append(f"Stale exception: {name}/{path}")
if failures:
    raise SystemExit("\n".join(failures))
print(f"Naming audit passed for {len(manifest['repositories'])} repositories; {len(seen)} reviewed external/historical lines.")

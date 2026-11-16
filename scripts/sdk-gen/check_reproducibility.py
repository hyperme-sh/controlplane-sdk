#!/usr/bin/env python3
"""Generate twice from the committed snapshot and reject byte or inventory drift."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from spanopticon_sdk_gen.rest_codegen import DEFAULT_IMAGE, REST_PRESETS, generate_rest_language, write_codegen_openapi
from spanopticon_sdk_gen.reproducibility import inventory, compare


def main() -> int:
    output = ROOT / '.cache/reproducibility'
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    canonical = inventory(ROOT / 'sdk/openapi')
    spec = write_codegen_openapi(ROOT, Path('sdk/openapi/v1/openapi.json'))
    subprocess.run(['docker', 'pull', DEFAULT_IMAGE], check=True)
    failures = []
    for language in sorted(REST_PRESETS):
        for attempt in ('first', 'second'):
            generate_rest_language(repo_root=ROOT, spec_rel=spec,
                out_rel=output.relative_to(ROOT) / attempt / language,
                language_key=language)
        first = inventory(output / 'first' / language)
        second = inventory(output / 'second' / language)
        failures.extend(f'{language} nondeterministic {m}' for m in compare(first, second))
        prefix = f'sdk/rest/{language}/'
        tracked = subprocess.check_output(['git', 'ls-files', '-z', '--', prefix], cwd=ROOT).decode().split('\0')
        committed = inventory(ROOT / prefix, [p.removeprefix(prefix) for p in tracked if p])
        failures.extend(f'{language} committed {m}' for m in compare(committed, first))
    failures.extend(f'canonical snapshot {m}' for m in compare(canonical, inventory(ROOT / 'sdk/openapi')))
    (output / 'result.json').write_text(json.dumps({'generator': DEFAULT_IMAGE, 'differences': failures}, indent=2) + '\n')
    print('\n'.join(failures) if failures else 'All four REST clients regenerate identically, twice; canonical snapshots unchanged.')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())

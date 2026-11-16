#!/usr/bin/env python3
"""Check owner provenance, real generation and both isolated gRPC consumers."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from spanopticon_sdk_gen.grpc_codegen import generate_python_grpc
from spanopticon_sdk_gen.reproducibility import inventory, compare


def main():
    source = ROOT / 'sdk/proto/spanopticon/v1/contractecho.proto'
    manifest = json.loads((ROOT / 'sdk/proto/provenance.json').read_text())
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    assert manifest['sha256'] == digest, 'Protocol snapshot hash mismatch'
    if '--verify-owner' in sys.argv:
        revision = manifest['revision']
        assert len(revision) == 40 and all(c in '0123456789abcdef' for c in revision)
        assert manifest['repository'] == 'hyperme-sh/controlplane-proto'
        assert manifest['path'] == 'proto/spanopticon/v1/contractecho.proto'
        url = f'https://raw.githubusercontent.com/hyperme-sh/controlplane-proto/{revision}/{manifest["path"]}'
        with urllib.request.urlopen(url, timeout=30) as response:
            assert response.read() == source.read_bytes(), 'Protocol owner snapshot mismatch'
    with tempfile.TemporaryDirectory() as directory:
        scratch = Path(directory)
        for attempt in ('first', 'second'):
            generate_python_grpc(ROOT, scratch / attempt)
        first = inventory(scratch / 'first')
        assert not compare(first, inventory(scratch / 'second')), 'Non-deterministic gRPC output'
        # The source-only proto and provenance stay outside the generated inventory.
        names = [p.relative_to(ROOT / 'sdk').as_posix()
                 for folder in ('proto/spanopticon/v1', 'grpc/python')
                 for p in (ROOT / 'sdk' / folder).rglob('*')
                 if p.suffix in ('.py', '.pyi')]
        expected = inventory(ROOT / 'sdk', names)
        assert not compare(expected, first), compare(expected, first)
        for base, layout in [(ROOT / 'sdk', 'committed'), (scratch / 'first', 'fresh')]:
            for suffix in ('proto/spanopticon/v1', 'grpc/python'):
                subprocess.run([sys.executable, '-I', str(ROOT / 'tests/grpc_consumer.py'),
                                str(base / suffix)], check=True)
            print(f'{layout}: both isolated Python gRPC import layouts passed')
    print('Protocol owner hash and deterministic flat/namespaced generation passed')


if __name__ == '__main__':
    main()

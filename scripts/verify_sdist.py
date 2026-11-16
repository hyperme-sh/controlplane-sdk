"""Verify all declared source-distribution files against tracked source bytes."""
from pathlib import Path
import subprocess
import sys
import tarfile

root = Path(__file__).resolve().parents[1]
paths = ['LICENSE','sdk','src','scripts','tests','docs','tools/grpc',
         'pyproject.toml','uv.lock','README.md','.gitignore',
         'packages/sea-device-link/src','packages/sea-device-link/README.md',
         'packages/sea-device-link/LICENSE']
names = subprocess.check_output(['git','ls-files','-z','--',*paths],cwd=root).decode().split('\0')
expected = {name:(root/name).read_bytes() for name in names if name}
archive_path, = Path(sys.argv[1]).glob('*.tar.gz')
with tarfile.open(archive_path) as archive:
    actual = {}
    for member in archive.getmembers():
        if member.isdir():
            continue
        if not member.isfile():
            raise ValueError(f'Unexpected source archive member: {member.name}')
        name = member.name.split('/',1)[1]
        if name in actual:
            raise ValueError(f'Duplicate source archive member: {name}')
        actual[name] = archive.extractfile(member).read()
    # PKG-INFO is build metadata, not a tracked source file.
    assert set(actual) == set(expected) | {'PKG-INFO'}, (set(expected)-set(actual),set(actual)-set(expected))
    for name, data in expected.items():
        assert actual[name] == data, name
print('Source archive inventory and bytes match all declared tracked inputs')

"""Check every wheel module against the generated client and helper sources."""
from pathlib import Path
import sys
import zipfile
root = Path(__file__).resolve().parents[1]
expected = {}
for base in (root / 'sdk/rest/python', root / 'src'):
    package = base / ('openapi_client' if base.name == 'python' else 'spanopticon_sdk_gen')
    expected.update({p.relative_to(base).as_posix(): p.read_bytes() for p in package.rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts})
wheel, = Path(sys.argv[1]).glob('*.whl')
with zipfile.ZipFile(wheel) as archive:
    names = archive.namelist()
    assert len(names) == len(set(names))
    assert {n for n in names if '.dist-info/' not in n} == set(expected)
    for name, data in expected.items():
        assert archive.read(name) == data, name
print('Wheel modules match source bytes')

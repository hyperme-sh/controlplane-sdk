"""Check every wheel module against the generated client and helper sources."""
from pathlib import Path
import sys
import zipfile
import tomllib
from email.parser import BytesParser
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
    project = tomllib.loads((root / 'pyproject.toml').read_text())['project']
    metadata_name, = [n for n in names if n.endswith('.dist-info/METADATA')]
    metadata = BytesParser().parsebytes(archive.read(metadata_name))
    assert metadata['Name'] == project['name']
    assert metadata['Version'] == project['version']
    assert metadata['License-Expression'] == project['license']
    license_name, = [n for n in names if n.endswith('.dist-info/licenses/LICENSE')]
    assert archive.read(license_name) == (root / 'LICENSE').read_bytes()
print('Wheel module bytes, package identity, version and license match root source')

from pathlib import Path
import tomllib
from spanopticon_sdk_gen.package_metadata import install_package_metadata


def test_metadata_keeps_identity_and_version_and_preserves_binary(tmp_path):
    root = tmp_path / 'generated'
    root.mkdir()
    license_source = tmp_path / 'LICENSE'
    license_source.write_text('Apache license text')
    (root / 'pyproject.toml').write_text('[tool.poetry]\nname="openapi-client"\nversion="1.0.0"\nlicense = "NoLicense"\nrepository="https://github.com/GIT_USER_ID/GIT_REPO_ID"\n')
    (root / 'binary.jar').write_bytes(b'\xff\x00\xfe')
    install_package_metadata(root,license_source)
    once = {p.name:p.read_bytes() for p in root.iterdir()}
    install_package_metadata(root,license_source)
    assert once == {p.name:p.read_bytes() for p in root.iterdir()}
    data=tomllib.loads((root/'pyproject.toml').read_text())['tool']['poetry']
    assert data['name']=='openapi-client' and data['version']=='1.0.0'
    assert data['license']=='Apache-2.0'
    assert data['repository']=='https://github.com/hyperme-sh/controlplane-sdk'
    assert (root/'binary.jar').read_bytes()==b'\xff\x00\xfe'

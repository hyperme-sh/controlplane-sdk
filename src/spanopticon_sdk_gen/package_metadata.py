"""Apply repository ownership metadata without changing package names or versions."""
from pathlib import Path

NOTICE = '''> Generated source tree; not a separately published package. Recorded template
> names and versions are retained. See the repository root for supported consumers
> and the `controlplane-sdk` Python distribution. This directory grants no release authority.

'''


def install_package_metadata(root: Path, license_source: Path) -> list[str]:
    changed = []
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        try:
            original = path.read_text()
        except UnicodeDecodeError:
            continue
        updated = original.replace('GIT_USER_ID', 'hyperme-sh').replace('GIT_REPO_ID', 'controlplane-sdk')
        if path.name == 'pyproject.toml':
            updated = updated.replace('license = "NoLicense"', 'license = "Apache-2.0"')
        if updated != original:
            path.write_text(updated)
            changed.append(path.relative_to(root).as_posix())
    readme = root / 'README.md'
    text = readme.read_text() if readme.exists() else '# Generated REST client\n'
    if not text.startswith(NOTICE):
        readme.write_text(NOTICE + text)
    (root / 'LICENSE').write_bytes(license_source.read_bytes())
    return changed + ['README.md', 'LICENSE']

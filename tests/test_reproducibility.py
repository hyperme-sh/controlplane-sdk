from pathlib import Path
import shutil

import pytest
from spanopticon_sdk_gen.reproducibility import inventory, compare
from spanopticon_sdk_gen.swift_portability import install_swift_portability
from spanopticon_sdk_gen.kotlin_auth import install_kotlin_auth

ROOT = Path(__file__).resolve().parents[1]


def test_inventory_detects_added_removed_and_changed_files(tmp_path):
    (tmp_path / 'kept').write_text('one')
    (tmp_path / 'removed').write_text('old')
    before = inventory(tmp_path)
    (tmp_path / 'kept').write_text('two')
    (tmp_path / 'removed').unlink()
    (tmp_path / 'added').write_text('new')
    assert compare(before, inventory(tmp_path)) == [
        'added: unexpected', 'kept: changed', 'removed: missing']


def test_inventory_rejects_links_and_missing_managed_files(tmp_path):
    (tmp_path / 'link').symlink_to('/etc/passwd')
    with pytest.raises(ValueError, match='Unsafe'):
        inventory(tmp_path)
    with pytest.raises(ValueError, match='Missing'):
        inventory(tmp_path, ['missing'])


@pytest.mark.parametrize('language,transform', [('swift5', install_swift_portability), ('kotlin', install_kotlin_auth)])
def test_native_transforms_are_repeatable_and_reject_template_drift(tmp_path, language, transform):
    source = ROOT / 'sdk/rest' / language
    # Only copy the transform inputs, not build output or generated test stubs.
    names = (['OpenAPIClient/Classes/OpenAPIs/URLSessionImplementations.swift',
              'OpenAPIClient/Classes/OpenAPIs/Validation.swift'] if language == 'swift5'
             else ['src/main/kotlin/org/openapitools/client/infrastructure/ApiClient.kt'])
    for name in names:
        dest = tmp_path / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / name, dest)
    expected = inventory(tmp_path)
    transform(tmp_path)
    transform(tmp_path)
    assert inventory(tmp_path) == expected
    (tmp_path / names[0]).write_text('changed generator template')
    with pytest.raises(ValueError, match='Unexpected'):
        transform(tmp_path)

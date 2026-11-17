"""Main package validation must not restore retired archive publication."""
from pathlib import Path


def test_main_keeps_validation_without_artifact_publication():
    root = Path(__file__).resolve().parents[1]
    workflow = (root / ".github/workflows/package.yml").read_text()
    assert not (root / ".github/workflows/release.yml").exists()
    for forbidden in ("upload-artifact", "RELEASE_ARTIFACT_DIR",
                      "packages: write", "docker push"):
        assert forbidden not in workflow
    for required in ("bash scripts/check-package.sh", "scripts/sdk-gen/check_breaking.py",
                     "contents: read", "branches: [main]", "debrunner", "ubuntu-24.04"):
        assert required in workflow

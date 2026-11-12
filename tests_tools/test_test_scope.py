"""The installed-edge suite is admitted only by its scheduled owner adapter."""
import os
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
NIGHTLY = dict(NIGHTLY_SUITE='sdk-consumers', GITHUB_ACTIONS='true',
               GITHUB_EVENT_NAME='schedule', GITHUB_REF='refs/heads/main',
               GITHUB_REPOSITORY='hyperme-sh/controlplane-sdk')


def selection(extra):
    env = {key: value for key, value in os.environ.items() if key not in NIGHTLY}
    env.update(extra)
    return subprocess.run(['bash', '-euc', 'source "$1"; printf "%s\\n" "${sdk_test_selection[@]}"',
                           'scope', str(ROOT / 'scripts/test-scope.sh')],
                          env=env, text=True, capture_output=True, check=False)


@pytest.mark.parametrize('event', ['pull_request', 'push', 'workflow_dispatch', ''])
def test_normal_preparation_keeps_contracts_without_installed_edge(event):
    result = selection({'GITHUB_EVENT_NAME': event})
    assert result.returncode == 0
    assert result.stdout.strip() == '--ignore=tests/test_edge_export_integration.py'


def test_registered_nightly_includes_the_complete_suite():
    result = selection(NIGHTLY)
    assert result.returncode == 0
    assert not result.stdout.strip()


@pytest.mark.parametrize(('key', 'value'), [
    ('NIGHTLY_SUITE', 'wrong-suite'), ('GITHUB_ACTIONS', 'false'),
    ('GITHUB_EVENT_NAME', 'workflow_dispatch'), ('GITHUB_EVENT_NAME', 'pull_request'),
    ('GITHUB_REF', 'refs/heads/topic'), ('GITHUB_REPOSITORY', 'other/sdk'),
])
def test_mislabeled_or_manual_runs_cannot_enable_exporter(key, value):
    result = selection({**NIGHTLY, key: value})
    assert result.returncode == 2
    assert 'central scheduled main' in result.stderr

# Sourced by package validation for all three artifact forms.
sdk_test_selection=(--ignore=tests/test_edge_export_integration.py)
if [[ -n "${NIGHTLY_SUITE:-}" ]]; then
  if [[ "$NIGHTLY_SUITE" != sdk-consumers || "${GITHUB_ACTIONS:-}" != true ||
        "${GITHUB_EVENT_NAME:-}" != schedule || "${GITHUB_REF:-}" != refs/heads/main ||
        "${GITHUB_REPOSITORY:-}" != hyperme-sh/controlplane-sdk ]]; then
    echo 'SDK exporter integration belongs to the central scheduled main batch' >&2
    return 2
  fi
  sdk_test_selection=()
fi

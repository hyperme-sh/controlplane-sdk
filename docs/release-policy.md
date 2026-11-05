# Release compatibility

`controlplane-sdk` is version **0.2.0**. [`release-policy.json`](../release-policy.json) and [`.github/workflows/release.yml`](../.github/workflows/release.yml) declare release line **0.2**. Components that share a Spanopticon release line share major and minor versions. Patch numbers advance on their own and keep the accepted API contract for that version.

`release-policy.json` names this repository and the version file `pyproject.toml`. The Spanopticon workflow checks that file on pull requests. A version change, or a `releases/candidate/release.json` submission, also goes through release admission. Tag pushes and manual release requests go through admission. A configuration-only result is a configuration check.

Channel layout, Actions artifacts, `test-<commit>` snapshots, and the published `v0.24.0` record are in [Releasing](releasing.md).

Before a release:

1. Put an accepted bundle at `releases/accepted/release.json`, with its contract files and immutable artifact references. Set the repository variable `SPANOPTICON_RELEASE_BASELINE_SHA` to that bundle's full 40-character commit SHA. The first baseline needs artifact and consumer evidence from the real build. Example digests are not release evidence.
2. Generate the candidate bundle at `releases/candidate/release.json` from the release artifacts. It contains this component, uses line `0.2`, and matches `pyproject.toml` plus the requested tag.
3. Run admission against the trusted baseline. A patch keeps the published contract. Replacing a published artifact at the same version fails admission. Check artifact provenance and downstream consumer behavior on their own.
4. Make that admission, and the artifact and consumer checks, prerequisites of the publisher for that exact release. Select the accepted baseline from the repository variable. Keep the validation evidence with the run.

A missing baseline fails admission. This workflow writes no deployment. It does not grant access to private dependencies, and it does not prove an artifact exists until the files are present. See the [Spanopticon release policy](https://github.com/hyperme-sh/spanopticon/blob/main/docs/releases.md) for the manifest format and compatibility rules.

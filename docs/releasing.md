# Releasing

Release mechanics for `controlplane-sdk`. Compatibility checks that run before a tag are in [Release compatibility](release-policy.md). The shared manifest format is the [Spanopticon release policy](https://github.com/hyperme-sh/spanopticon/blob/main/docs/releases.md).

## Versions in this tree

| Record | Value |
| --- | --- |
| Python package (`pyproject.toml`) | `controlplane-sdk` 0.2.0 |
| Release line (`release-policy.json`, `.github/workflows/release.yml`) | `0.2` |
| OpenAPI document (`sdk/openapi/v1/openapi.json` `info.version`) | `1.0.0` |
| Generated `openapi_client` placeholder | `1.0.0` (generator metadata; the distribution version is 0.2.0) |

## What main validation stores

[`.github/workflows/package.yml`](../.github/workflows/package.yml) runs `bash scripts/check-package.sh` on `main`. On a main push it uploads the wheel and sdist that the check just built as the `tested-dist` artifact, uncompressed, retained for 90 days. It also uploads the source, wheel, and rebuilt-sdist JUnit files as `test-results`, retained for 90 days. That workflow's permissions are `contents: read`. GitHub releases and tags are produced by the stable publisher below.

The package check exports packaged runtime and resource bytes from the wheel without importing the candidate, binds that build's version and digest, and compares the contract rebuilt from the sdist. Byte equality includes implementation changes that alter packaged files. Installer-metadata compatibility and live consumer behavior are separate checks. Kotlin, Swift, TypeScript, and gRPC trees are outside the root wheel contract.

The OpenAPI snapshot smoke test is part of the source, wheel, and rebuilt-sdist runs. The check rejects a skipped test or a test inventory that differs across those three runs. Public package jobs run on `ubuntu-24.04`.

## Test snapshots

Tags of the form `test-<commit>` are development snapshots. The package version embedded in a snapshot is the version that was built for that commit. It does not reserve a later stable version number.

Evidence lives under [`releases/qualification`](../releases/qualification). The snapshot at `releases/qualification/snapshots/29bba853f13800204cfaec96f967f25e85cd303c` is recorded with `"stable_release": false` and live tag `test-29bba853f13800204cfaec96f967f25e85cd303c`. Package CI still checks the wheel built from the current tree against that layout when a qualification manifest is present.

## Stable release record

[`releases/accepted`](../releases/accepted) and the repository variable `SPANOPTICON_RELEASE_BASELINE_SHA` are the stable channel. A test snapshot stays under `releases/qualification`.

The accepted record binds the published GitHub release [v0.24.0](https://github.com/hyperme-sh/controlplane-sdk/releases/tag/v0.24.0):

| Field | Value |
| --- | --- |
| Tag | `v0.24.0` |
| Source revision | `7fc4d86fdce125b45ef954d21541b981987e6cf9` |
| Release id | `434676742` |
| Baseline commit | `fbeaf6601fe7f16bde4f43f85de400bdd9d80926` |
| `controlplane_sdk-0.24.0-py3-none-any.whl` | `sha256:7464a13468f17f577d970285e94f1c1cee6916687634e5afe480404e29469987` |
| `controlplane_sdk-0.24.0.tar.gz` | `sha256:5bb70e986e5a30bdfa27f2f916d33e5ad002cf76948a6ed3ba7593384a3bd267` |
| `release-manifest.json` | `sha256:9788901764cb674daa3c4d18ee173d17686eea231c6dfb9c1bb3c3e4fe46d990` |

`releases/accepted/release.json` records that publication on line `0.24`, component version `0.24.0`. The checkout you clone today is package **0.2.0** on line **0.2**. Installing this tree builds 0.2.0. The table above identifies the already published `v0.24.0` artifacts and the baseline commit stored with that record. Deploying a consumer of either build is a separate step from recording the artifact.

## Stable publication

A stable tag has the form `vMAJOR.MINOR.PATCH`. [`.github/workflows/release.yml`](../.github/workflows/release.yml) runs on those tags. It admits the release on line `0.2` against `SPANOPTICON_RELEASE_BASELINE_SHA`, then publishes the exact files retained by the package workflow. The publisher checks that baseline and leaves `test-<commit>` snapshots on the test channel.

The admission workflow is `hyperme-sh/spanopticon/.github/workflows/component-release.yml` at `32c064be9fe47e230e0d48d353ada8b38a7c1644`. The publish action is `hyperme-sh/.github/actions/release-channel` at `c16044a6d987d7d912d70bcd09ea731ab2b91b9e`.

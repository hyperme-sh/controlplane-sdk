# Control plane SDK

## Current version authority

Current development version: `0.2.0`. The services remain before the unreleased
0.24.0 milestone. Earlier 0.24/1.0 preparation and publication notes below are
historical and do not authorize those versions. Existing tags and historical
artifacts remain untouched. Development uses exact source pins and rebuilt
artifacts; no prior release is required. Version changes, tags and publication
require the owner's explicit authorization to the agent.

Generated REST clients, protocol snapshots, auth examples and generation helpers.
The root Python distribution `controlplane-sdk` installs `openapi_client` and
`spanopticon_sdk_gen`. It must not be installed alongside another distribution
providing the same `openapi_client` namespace. The root distribution uses the coordinated 0.24 line and immutable test releases.

Use Python 3.13 and uv 0.11.26:

    uv sync --frozen
    bash scripts/check-package.sh

Checks exercise generation helpers and the installed Python client from source,
a fresh wheel, and a rebuilt source distribution. Generated test placeholders
under sdk/rest/python/test are not counted as behavioral coverage.

The sdk/ tree retains TypeScript, Python, Kotlin and Swift REST sources, Python
gRPC stubs, protocol inputs and auth examples. Only the Python REST client and
helper modules are in the root wheel. Other languages and gRPC are retained
artifacts, not independently qualified releases. Generated manifests retain
upstream placeholder metadata; use the root Python build for validation.

The committed OpenAPI is a snapshot, not a claim of current server compatibility.
Refreshing it requires complete owner-service contract export and reconciliation.
See scripts/sdk-gen/README.md for REST generation and structural removal checks.
Multilanguage compilation, actual regeneration, gRPC/proto synchronization,
auth examples and consumer acceptance remain separate qualification gates.

CI uses pinned actions, read-only permissions and main/manual triggers. Actions
is enabled; exact-head hosted-runner qualification remains separate from the
local package checks. A separate read-only hosted PR workflow qualifies the Python distribution.
No source service, release publication or deployment is changed by this package.

AI inference/session and usage clients have separate case-safe names. `AIApi`
retains the original inference/session operations; `AIUsageApi` owns usage history
and summary. `AiApi` and previous usage-module imports remain compatibility aliases.
All four REST trees are regenerated with complete snapshot method/path checks.
See [the adoption evidence](docs/ai-usage-adoption.md). Shared-runner CI acceptance
is #2; native language compilation and deployed consumer qualification remain #3.

See [the organization naming migration](docs/spanopticon-migration.md) for linked PRs, rollout order, validation and the repeatable audit.

## Release channels

Main validation retains its exact qualified files in Actions artifacts. It does
not create GitHub releases or tags. Historical `test-<commit>` prereleases remain
qualification evidence and do not establish an accepted stable release.

Stable publication requires an explicit `vMAJOR.MINOR.PATCH` tag, the exact
successful main validation artifact, compatible declared contracts and an actual
immutable stable baseline. The publisher independently verifies that evidence;
successful caller jobs alone cannot establish acceptance. Missing evidence and
first-stable bootstrap remain closed. Package qualification, coordinated consumer
acceptance and runtime deployment remain separate.

## Artifact contracts

The root distribution is version 0.24.0. CI exports all packaged runtime/resource
bytes from the actual wheel without importing candidate code, binds the candidate
version and digest to that build, and compares rebuilt-sdist contracts. Conservative
byte equality rejects implementation-only patch changes as well. Installer-metadata
and semantic compatibility remain separate; archived owner/multilanguage artifacts
are not counted as independently qualified by the root package tests.

## Test qualification and stable acceptance

GitHub `test-<commit>` prereleases are development snapshots. Their embedded
package version does not reserve a stable version. Artifact and consumer evidence
lives under `releases/qualification`; the current wheel binding is still checked
by package CI, alongside any future explicit stable candidate. Earlier test
snapshot receipts are preserved there with an explicit non-stable classification.

`releases/accepted` and `SPANOPTICON_RELEASE_BASELINE_SHA` are reserved for an
actual immutable stable GitHub release. The pinned shared guard verifies the live
release channel, stable tag source and asset digests; a test snapshot cannot
become accepted through a provenance label. The accepted record now binds the
already published immutable `v0.24.0` release to its actual source and asset
digests. The independently selected baseline is
`fbeaf6601fe7f16bde4f43f85de400bdd9d80926`. Test qualification history remains
separate. This records an existing distribution; runtime deployment and
coordinated consumer acceptance remain separate.

### Actions qualification and stable publication

Main merges and workflow completion do not publish GitHub test releases. Exact
qualification files remain in Actions artifacts with finite retention. The pinned
publisher independently verifies a real immutable stable baseline and refuses
qualification snapshots, even if a caller job reports success. Existing valid
stable records are retained; no release, version change, deployment or human
approval prerequisite is introduced by this correction.

## Public license and executed test inventory

The repository and root Python distribution are Apache-2.0 licensed; dependencies
retain their own licenses. Generated client placeholders are not separate supported
release metadata. The OpenAPI snapshot smoke test is required in source, wheel
and rebuilt-sdist qualification. CI rejects skips or unequal test inventories.
Public jobs use hosted Ubuntu and private jobs use debrunners.

## Installed-edge offline export qualification

The development graph pins the public edge owner at an immutable revision.
Two previously excluded Panopticon tests now exercise real installed-edge OpenAPI
export and byte-preserving synchronization in source, wheel and rebuilt-sdist
contexts. Their environment has no upstream URLs or deployment configuration, and
unexpected HTTP requests fail. This validates offline behavior, not a complete
live-service contract snapshot. Client runtime dependencies remain unchanged.

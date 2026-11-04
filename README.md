# Control plane SDK

Generated REST clients, protocol snapshots, auth examples and generation helpers.
The root Python distribution `controlplane-sdk` installs `openapi_client` and
`spanopticon_sdk_gen`. It must not be installed alongside another distribution
providing the same `openapi_client` namespace. No package has been published.

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
local package checks. No PR-triggered package workflow is configured.
No source service, release publication or deployment is changed by this package.

AI inference/session and usage clients have separate case-safe names. `AIApi`
retains the original inference/session operations; `AIUsageApi` owns usage history
and summary. `AiApi` and previous usage-module imports remain compatibility aliases.
All four REST trees are regenerated with complete snapshot method/path checks.
See [the adoption evidence](docs/ai-usage-adoption.md). Shared-runner CI acceptance
is #2; native language compilation and deployed consumer qualification remain #3.

See [the organization naming migration](docs/spanopticon-migration.md) for linked PRs, rollout order, validation and the repeatable audit.

## Release channels

Successful main-push validation retains the validated Python wheel and source distribution and publishes
an immutable `test-<commit>` GitHub prerelease. Push a `vMAJOR.MINOR.PATCH`
tag at that tested commit to promote the exact files to a stable release,
without rebuilding. Repository visibility applies to all package assets.
Package metadata versions are preserved; these are GitHub distribution snapshots,
not automatic PyPI publication or service deployment.

Promotion requires the original Actions artifact (90-day requested retention;
organization policy may shorten it). Expired evidence fails closed: validate a
new main revision. The publisher verifies the run, source, workflow and artifact
digest independently of release metadata. Repository immutable releases must be
enabled. See the [shared release contract](https://github.com/hyperme-sh/.github/blob/7749591fccd30d46ba9b0adabe82114001c9d0de/actions/release-channel/README.md).

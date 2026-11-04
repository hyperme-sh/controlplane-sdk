# Control plane SDK

Generated REST clients, protocol snapshots, auth examples and generation helpers.
The root Python distribution `controlplane-sdk` installs `openapi_client` and
`panopticon_sdk_gen`. It must not be installed alongside another distribution
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
remains disabled until hosted-worker policy and an exact-head run are qualified.
No source service, release publication or deployment is changed by this package.

The snapshot contained broken imports for a nonexistent AiApi class. Those
exports are removed; AIApi remains available. Tag collision and complete
operation coverage qualification remain tracked in #4. Hosted CI acceptance
is #2; regeneration, language toolchains and consumer acceptance are #3.

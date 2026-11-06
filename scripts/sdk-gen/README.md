# SDK generation tools

REST generation reads [`sdk/openapi/v1/openapi.json`](../../sdk/openapi/v1/openapi.json) through `generate_rest_sdks.py`. The script expects the OpenAPI Generator Docker image to be present locally. `check_breaking.py` compares paths and schema names with an explicit `--baseline-file`. The comparison is structural: paths and schema names.

Exporting a fresh OpenAPI document from the control plane, regenerating gRPC stubs, and compiling Kotlin or Swift are separate from this script. Offline export uses the `controlplane-edge` package and its configuration. A complete consumer contract is the exported control plane document plus these generated clients.

A missing baseline fails the check. `--allow-missing-baseline` is the bootstrap opt-in for a first snapshot. An omitted `--baseline-file` fails. A structural removal check is one input to a patch release. A Spanopticon release also carries the exported protocol and library contracts and the control plane consumer tests. See [Releasing](../../docs/releasing.md).

## Case-safe AI generation

The generator maps the `ai` tag to `AIUsage` and keeps the canonical HTTP paths and the snapshot. Python, TypeScript, Kotlin, and Swift keep both inference/session operations and usage operations, plus the legacy usage-client aliases. Generation checks every snapshot method and path in a clean staging directory before it replaces manifest-managed files. Custom files stay. Obsolete managed files are removed. TypeScript barrel request types that would collide are also exported with their API prefix. Module-local names stay as they are.

The default generator is digest-pinned OpenAPI Generator 7.10.0. Pull that image before running. The generator uses `--pull=never`. From the repository root:

```sh
uv run --frozen python scripts/sdk-gen/generate_rest_sdks.py
bash scripts/check-package.sh
```

The package check covers operation coverage, every Python import, the compatibility aliases, and loopback HTTP from the source tree, the wheel, and the rebuilt sdist. The loopback server is a local contract fixture. Kotlin and Swift native builds, a refresh of `sdk/openapi/v1/openapi.json` from a live control plane, and a deployed consumer are covered with a release. The generator writes the REST trees under `sdk/rest` and leaves release tags and the package registry unchanged.

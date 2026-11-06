# AI client names

Inference and session calls live on `AIApi`. Usage history and summary live on `AIUsageApi`. `AiApi` is an alias of `AIUsageApi`, so older imports keep working. HTTP paths are unchanged.

The generator change landed in this repository from control-plane commits `aa552c8b5b2912283064ce15364b919e0f740e66` and `7356887667b0f142bac7504223ebf9446e0f5411`. The public client is [hyperme-sh/controlplane-sdk](https://github.com/hyperme-sh/controlplane-sdk). Those commits were merged on top of `7a851c5` in this repository.

`spanopticon_sdk_gen` stays the helper package. The script imports this repository's `src` tree. The OpenAPI snapshot in `sdk/openapi/v1/openapi.json` was left as committed.

The generator maps usage operations to `AIUsage` and inference/session operations to `AI`. It checks all 131 canonical method/path operations, including all 11 AI operations, in Python, TypeScript, Kotlin, and Swift before writing output. Usage entrypoints stay as aliases, with distinct filenames. Obsolete manifest-managed files are removed. Custom gateway files stay outside that operation inventory. The TypeScript barrel exports colliding request interfaces under an API prefix and keeps the module-local names.

## What was run

- Generator image: `openapitools/openapi-generator-cli@sha256:f2054a5a7908ad81017d0f0839514ba5eab06ae628914ff71554d46fac1bcf7a` (7.10.0).
- All four languages were regenerated from this snapshot. A second run matched the first byte for byte. The snapshot file was unchanged.
- `scripts/check-package.sh`: 34 tests from source, from an installed wheel, and from a rebuilt sdist. Wheel bytes matched the source tree. The run imports every Python module, checks the method/path inventory, and calls inference and usage on a loopback server with typed responses, captured headers, and the legacy usage aliases.
- The TypeScript public entrypoint compiled with TypeScript, target ES2020, lib DOM.
- The wheel was also run against the AI service's loopback HTTP and PostgreSQL inference, history, and summary test. Authorization and upstream inference in that test are fixtures.

Kotlin and Swift native compilation, a new protobuf export, and a deployed AI service are separate from this package check. Regenerate with the commands in [SDK generation tools](../scripts/sdk-gen/README.md).

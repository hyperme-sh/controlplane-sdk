# SDK generation tools

REST generation consumes sdk/openapi/v1/openapi.json using generate_rest_sdks.py.
It requires a locally available OpenAPI Generator Docker image. check_breaking.py
compares paths and schema names against an explicit --baseline-file. This is a
structural check, not full semantic compatibility validation.

Owner OpenAPI export, gRPC regeneration and language toolchain qualification
remain separate integration work. The codegen helpers retain their original
owner API; offline export requires the owner edge package and configuration.
Do not use an offline stub as evidence of a complete consumer contract.

Missing baselines fail unless the caller explicitly uses `--allow-missing-baseline`
for initial bootstrap. That opt-in does not establish compatibility. A missing
explicit `--baseline-file` always fails. Structural removal checks do not qualify
patch releases: release promotion also needs the coordinated Spanopticon bundle
gate, exported protocol/library contracts and owner consumer tests.


## Case-safe AI generation

The generator-only copy maps the `ai` tag to `AIUsage`, preserving canonical
HTTP paths and the snapshot. Python, TypeScript, Kotlin and Swift retain both
inference/session and usage operations with legacy usage-client aliases.
Generation validates every snapshot method/path in a clean staging directory
before replacing manifest-managed artifacts. Custom files are preserved, and
obsolete managed files are pruned. TypeScript barrel request types that collide
are additionally available with their API prefix; module-local names remain.

The default generator is digest-pinned OpenAPI Generator 7.10.0. Pull that image
explicitly before running; the generator uses `--pull=never`. From the repo root:

```sh
uv run --frozen python scripts/sdk-gen/generate_rest_sdks.py
bash scripts/check-package.sh
```

The package checks run operation coverage, all Python imports, compatibility
aliases and real loopback HTTP transport from source, wheel and rebuilt sdist.
The loopback server is a contract fixture, not a deployed owner. Native Kotlin
and Swift builds, current owner contract refresh and deployed acceptance remain
release gates; this command does not publish or commit generated output.

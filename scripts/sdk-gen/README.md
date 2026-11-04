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

# AI client adoption from source PR #724

This ports the reviewed generator and SDK changes from
[FyberLabs/panopticon#724](https://github.com/FyberLabs/panopticon/pull/724).
The source is merged as `aa552c8b5b2912283064ce15364b919e0f740e66`;
implementation provenance is reviewed source head
`7356887667b0f142bac7504223ebf9446e0f5411`, which includes that merge.
The destination base is `7a851c5` from this repository's main branch.

The implementation retains this repository's `spanopticon_sdk_gen` package,
existing installed-client packaging, canonical namespace and separate protocol
artifacts. It does not import monorepo workspace dependencies or refresh the
OpenAPI snapshot. The script imports from this repository's `src` tree.

The generator maps usage to `AIUsage`, retains inference/session `AI`, and checks
all 131 canonical method/path operations, including all 11 AI operations, in each
of Python, TypeScript, Kotlin and Swift before installing output. Existing usage
entrypoints remain aliases without case-only filenames. Only obsolete
manifest-managed files are removed; custom Gateway files remain outside the
canonical operation inventory. The TypeScript barrel also disambiguates duplicate
request interfaces while retaining module-local names.

## Validation

- Pinned generator: `openapitools/openapi-generator-cli@sha256:f2054a5a7908ad81017d0f0839514ba5eab06ae628914ff71554d46fac1bcf7a` (7.10.0).
- All four languages regenerated from the destination snapshot; a second run is
  byte-identical. The canonical snapshot is unchanged.
- `scripts/check-package.sh`: 34 tests from source, an installed wheel and a
  rebuilt sdist. Wheel contents match source bytes. This includes imports of
  every Python module, method/path inventory and loopback inference/usage calls
  with typed responses, captured headers and legacy usage aliases.
- The TypeScript public entrypoint compiles with TypeScript using ES2020/DOM.
- The installed component wheel is also qualified against the reviewed source
  AI-service owner harness using its real loopback HTTP and migrated PostgreSQL
  inference/history/summary test. Authorization and upstream inference are
  fixtures; this does not qualify the extracted AI service's installed runtime.

Native Kotlin/Swift compilation, owner-service/proto refresh, hosted CI and
actual deployed consumers remain separately qualified gates under issues #2/#3.
No package is published, client deployed, action enabled or workflow policy changed.
The source adoption addresses #14 and the case-collision source requirements in
#4; it is not a claim that every language is a qualified release.

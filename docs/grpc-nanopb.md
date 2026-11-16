# Embedded C / nanopb scope

The shared source is [contractecho.proto](../sdk/proto/spanopticon/v1/contractecho.proto),
package `spanopticon.v1`. This repository does not ship a generated C client or
claim embedded-target support. Python gRPC qualification does not qualify nanopb.

An embedded consumer needs a separately pinned protoc/nanopb toolchain, an options
file assigning bounded sizes to every string, compatible Timestamp handling, and
unit/contract tests for field presence, truncation/refusal and memory limits on its
selected target. No target or bounds have been selected here. Preserve field
numbers and distinguish omitted optional values from explicit zero/empty values.
Use the protocol owner's source revision recorded in `sdk/proto/provenance.json`;
do not invent a parallel message schema. No C package release is implied.

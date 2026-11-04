# C / nanopb (embedded)

Generate static C code from the same protos as Python:

- Protobuf sources: ``sdk/proto/spanopticon/v1/*.proto``
- Follow the repository root ``docs/grpc-nanopb.md`` for ``protoc`` + nanopb plugin and options files.

OpenAPI-based C clients are not generated here; protobuf is preferred for constrained devices.

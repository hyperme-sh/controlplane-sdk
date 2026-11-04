"""Copy protobuf sources and generate Python gRPC stubs under ``sdk/grpc/``."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def copy_proto_tree(repo_root: Path, sdk_proto_root: Path) -> None:
    """Copy ``proto/spanopticon`` into ``sdk/proto/spanopticon`` for consumers and nanopb."""

    src = repo_root / "proto" / "spanopticon"
    dst = sdk_proto_root / "spanopticon"
    if not src.is_dir():
        raise FileNotFoundError(f"missing proto tree: {src}")
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)


def _grpc_tools_proto_include() -> str:
    import grpc_tools

    return str(Path(grpc_tools.__file__).resolve().parent / "_proto")


def generate_python_grpc(
    repo_root: Path,
    out_sdk: Path,
    *,
    proto_rel: str = "proto/spanopticon/v1/contractecho.proto",
) -> None:
    """Run ``grpc_tools.protoc`` for Python into ``sdk/grpc/python``."""

    out_dir = out_sdk / "grpc" / "python"
    out_dir.mkdir(parents=True, exist_ok=True)
    proto_abs = repo_root / proto_rel
    if not proto_abs.is_file():
        raise FileNotFoundError(proto_abs)
    rel_from_proto_root = proto_abs.relative_to(repo_root / "proto")
    inc_grpc = _grpc_tools_proto_include()
    cmd = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        "-I",
        str(repo_root / "proto"),
        "-I",
        inc_grpc,
        f"--python_out={out_dir}",
        f"--grpc_python_out={out_dir}",
        str(rel_from_proto_root),
    ]
    subprocess.check_call(cmd, cwd=repo_root)


def write_c_nanopb_readme(sdk_root: Path) -> None:
    """Embedded C uses nanopb against the same ``.proto`` files; see docs/grpc-nanopb.md."""

    p = sdk_root / "grpc" / "c-nanopb-README.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        """# C / nanopb (embedded)

Generate static C code from the same protos as Python:

- Protobuf sources: ``sdk/proto/spanopticon/v1/*.proto``
- Follow the repository root ``docs/grpc-nanopb.md`` for ``protoc`` + nanopb plugin and options files.

OpenAPI-based C clients are not generated here; protobuf is preferred for constrained devices.
""",
        encoding="utf-8",
    )

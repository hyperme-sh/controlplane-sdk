"""Generate retained Python gRPC clients from the standalone protocol snapshot."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

PROTO_REL = Path('sdk/proto/spanopticon/v1/contractecho.proto')


def copy_proto_tree(repo_root: Path, sdk_proto_root: Path) -> None:
    """Copy protocol source only, without deleting unrelated destination files."""
    source = repo_root / PROTO_REL
    if not source.is_file():
        raise FileNotFoundError(source)
    target = sdk_proto_root / 'spanopticon/v1/contractecho.proto'
    if source.resolve() == target.resolve():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def _grpc_tools_proto_include() -> str:
    import grpc_tools
    return str(Path(grpc_tools.__file__).resolve().parent / '_proto')


def generate_python_grpc(repo_root: Path, out_sdk: Path, *,
                         proto_rel: str = str(PROTO_REL)) -> None:
    """Generate both historical flat and namespaced imports, plus typing stubs."""
    source = repo_root / proto_rel
    if not source.is_file():
        raise FileNotFoundError(source)
    proto_root = source.parents[2]
    for include, output in [(source.parent, out_sdk / 'proto/spanopticon/v1'),
                            (proto_root, out_sdk / 'grpc/python')]:
        output.mkdir(parents=True, exist_ok=True)
        subprocess.run([sys.executable, '-m', 'grpc_tools.protoc',
            '-I', str(include), '-I', _grpc_tools_proto_include(),
            f'--python_out={output}', f'--pyi_out={output}',
            f'--grpc_python_out={output}', str(source.relative_to(include))],
            cwd=include, check=True)


def write_c_nanopb_readme(sdk_root: Path) -> None:
    """Document the source-only embedded-C option without implying qualification."""
    path = sdk_root / 'grpc/c-nanopb-README.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('''# C / nanopb (source-only option)

The shared protocol source is `sdk/proto/spanopticon/v1/contractecho.proto`.
No generated C client, nanopb toolchain or embedded-target qualification is
supplied by this SDK. See [scope and prerequisites](../../docs/grpc-nanopb.md).
''')

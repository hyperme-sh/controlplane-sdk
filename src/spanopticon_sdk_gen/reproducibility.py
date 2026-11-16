"""Byte and inventory comparisons for generated clients, with no ignored files."""
from hashlib import sha256
from pathlib import Path


def inventory(root: Path, names: list[str] | None = None) -> dict[str, str]:
    paths = sorted(root.rglob('*')) if names is None else [root / n for n in names]
    result = {}
    for path in paths:
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Unsafe generated path: {path}')
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f'Missing generated file: {path}')
        result[path.relative_to(root).as_posix()] = sha256(path.read_bytes()).hexdigest()
    return result


def compare(expected: dict[str, str], actual: dict[str, str]) -> list[str]:
    return [f'{name}: ' + ('unexpected' if name not in expected else
            'missing' if name not in actual else 'changed')
            for name in sorted(expected.keys() | actual.keys())
            if expected.get(name) != actual.get(name)]

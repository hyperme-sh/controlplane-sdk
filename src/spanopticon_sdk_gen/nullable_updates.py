"""Retain unset versus explicit-null semantics in generated update models."""
import ast
from pathlib import Path

HELPER = '''"""Wire helpers for generated nullable update models."""


def with_explicit_nulls(model, values, nullable):
    for name, field in type(model).model_fields.items():
        wire = field.alias or name
        if wire in nullable and name in model.model_fields_set and getattr(model, name) is None:
            values[wire] = None
    return values


def restore_fields_set(model, source):
    present = {name for name, field in type(model).model_fields.items()
               if name in source or (field.alias or name) in source}
    model.model_fields_set.intersection_update(present)
    return model
'''


def nullable(schema):
    return (schema.get('nullable') is True or schema.get('type') == 'null'
            or isinstance(schema.get('type'), list) and 'null' in schema['type']
            or any(part.get('type') == 'null' for key in ('anyOf', 'oneOf')
                   for part in schema.get(key, []) if isinstance(part, dict)))


def install_nullable_updates(root: Path, document: dict) -> list[str]:
    schemas = document.get('components', {}).get('schemas', {})
    required = {name: tuple(k for k, v in schema.get('properties', {}).items() if nullable(v))
                for name, schema in schemas.items() if 'Update' in name or 'Patch' in name}
    required = {name: fields for name, fields in required.items() if fields}
    written, found = [], set()
    for path in sorted((root/'openapi_client/models').glob('*.py')):
        text = path.read_text()
        classes = [n.name for n in ast.parse(text).body if isinstance(n, ast.ClassDef) and n.name in required]
        if not classes:
            continue
        if len(classes) != 1:
            raise ValueError('Ambiguous generated update model')
        name = classes[0]
        found.add(name)
        if 'from openapi_client._nullable_updates import ' in text:
            continue
        if text.count('        return _dict\n') != 1 or text.count('        return _obj\n') != 1 or 'import json\n' not in text:
            raise ValueError('Generated update serialization layout changed: '+name)
        text = text.replace('import json\n', 'import json\nfrom openapi_client._nullable_updates import with_explicit_nulls, restore_fields_set\n', 1)
        text = text.replace('        return _dict\n', f'        return with_explicit_nulls(self, _dict, {required[name]!r})\n')
        text = text.replace('        return _obj\n', '        return restore_fields_set(_obj, obj)\n')
        path.write_text(text)
        written.append(path.relative_to(root).as_posix())
    if found != set(required):
        raise ValueError('Missing generated update models: '+', '.join(sorted(set(required)-found)))
    if required:
        helper = root/'openapi_client/_nullable_updates.py'
        helper.write_text(HELPER)
        written.append(helper.relative_to(root).as_posix())
    return written

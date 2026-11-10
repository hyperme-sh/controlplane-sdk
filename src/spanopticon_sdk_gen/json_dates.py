"""Install date-aware JSON helpers without changing generated wire dictionaries."""
from pathlib import Path

HELPER = '''"""Date encoding shared by generated model JSON helpers."""
from datetime import date, datetime
import json


def _date(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def model_json(value):
    return json.dumps(value, default=_date)
'''


def install_json_dates(root: Path) -> list[str]:
    """Patch clean generator output, retaining each model's to_dict semantics."""
    written = []
    replacements = {
        'return json.dumps(self.to_dict())': 'return model_json(self.to_dict())',
        'return json.dumps(self.actual_instance)': 'return model_json(self.actual_instance)',
    }
    for path in sorted((root / 'openapi_client/models').glob('*.py')):
        original = path.read_text()
        updated = original
        for before, after in replacements.items():
            updated = updated.replace(before, after)
        if updated == original:
            continue
        if 'import json\n' not in updated:
            raise ValueError('Generated JSON model import layout changed')
        updated = updated.replace('import json\n', 'import json\nfrom openapi_client._json_dates import model_json\n', 1)
        path.write_text(updated)
        written.append(path.relative_to(root).as_posix())
    if written:
        helper = root / 'openapi_client/_json_dates.py'
        helper.write_text(HELPER)
        written.append(helper.relative_to(root).as_posix())
    return written

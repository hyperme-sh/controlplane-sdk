"""Date encoding shared by generated model JSON helpers."""
from datetime import date, datetime
import json


def _date(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def model_json(value):
    return json.dumps(value, default=_date)

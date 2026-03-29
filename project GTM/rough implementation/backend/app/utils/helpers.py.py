import uuid
import hashlib
import json
from datetime import datetime

def generate_task_id() -> str:
    return str(uuid.uuid4())

def hash_data(data: dict) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def parse_date(date_str: str) -> datetime:
    try:
        return datetime.fromisoformat(date_str)
    except:
        return datetime.utcnow()

def format_currency(amount: float) -> str:
    return f"{amount:,.2f} ₽"
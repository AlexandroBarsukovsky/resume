# backend/app/services/script1_bridge.py
import redis
import json
import uuid
from datetime import datetime
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def publish_task(source: str, target: str, payload: dict, priority: str = "normal", ttl: int = 3600) -> str:
    task_id = str(uuid.uuid4())
    task_data = {
        "task_id": task_id,
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "target": target,
        "payload": payload,
        "priority": priority,
        "ttl": ttl,
        "retry_count": 0,
        "status": "pending"
    }
    redis_client.xadd("tasks_stream", {"data": json.dumps(task_data)})
    return task_id
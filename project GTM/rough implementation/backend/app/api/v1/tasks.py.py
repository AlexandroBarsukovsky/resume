from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
import uuid
import redis
import json
from app.core.config import settings
from app.core.dependencies import get_redis

router = APIRouter()

class TaskCreate(BaseModel):
    source: str
    target: str
    payload: dict
    priority: str = "normal"
    ttl: int = 3600

@router.post("/")
async def create_task(task: TaskCreate, redis_client=Depends(get_redis)):
    task_id = str(uuid.uuid4())
    task_data = {
        "task_id": task_id,
        "timestamp": datetime.utcnow().isoformat(),
        "source": task.source,
        "target": task.target,
        "payload": task.payload,
        "priority": task.priority,
        "ttl": task.ttl,
        "retry_count": 0,
        "status": "pending"
    }
    redis_client.xadd("tasks_stream", {"data": json.dumps(task_data)})
    return {"task_id": task_id, "status": "accepted"}

@router.get("/{task_id}")
async def get_task_status(task_id: str):
    return {"task_id": task_id, "status": "unknown"}

@router.post("/{task_id}/ack")
async def ack_task(task_id: str):
    return {"status": "ok"}
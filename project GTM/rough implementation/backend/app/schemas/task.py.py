from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime

class TaskCreate(BaseModel):
    source: str
    target: str
    payload: Dict[str, Any]
    priority: str = "normal"
    ttl: int = 3600

class TaskResponse(BaseModel):
    task_id: str
    status: str
    created_at: Optional[datetime] = None
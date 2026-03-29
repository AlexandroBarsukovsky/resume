from pydantic import BaseModel
from typing import Dict, Any

class AgentRunRequest(BaseModel):
    params: Dict[str, Any] = {}
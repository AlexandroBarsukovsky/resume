from pydantic import BaseModel
from typing import Optional

class AccountResponse(BaseModel):
    id: str
    name: str
    account_score: float
    health_score: float
    risk_flag: bool
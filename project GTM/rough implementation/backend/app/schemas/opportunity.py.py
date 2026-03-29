from pydantic import BaseModel
from typing import Optional

class OpportunityResponse(BaseModel):
    id: str
    account_id: str
    stage: str
    win_probability: float
    amount: float
    forecast_category: Optional[str]
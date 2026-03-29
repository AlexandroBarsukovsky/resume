from pydantic import BaseModel

class BudgetCheckRequest(BaseModel):
    article: str
    amount: float
    reason: str
    source_agent: str
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.budget import Budget

router = APIRouter()

class BudgetCheckRequest(BaseModel):
    article: str
    amount: float
    reason: str
    source_agent: str

@router.post("/check")
async def check_budget(req: BudgetCheckRequest, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.article == req.article).first()
    if not budget:
        raise HTTPException(404, "Article not found")
    available = budget.limit_amount - budget.spent
    if req.amount > available:
        return {"allowed": False, "available": available, "message": "Превышение лимита"}
    return {"allowed": True, "available": available - req.amount}

@router.post("/commit")
async def commit_budget(req: BudgetCheckRequest, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.article == req.article).first()
    if not budget:
        raise HTTPException(404, "Article not found")
    budget.spent += req.amount
    db.commit()
    return {"status": "committed"}
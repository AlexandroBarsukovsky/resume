# backend/app/services/script2_treasury.py
from sqlalchemy.orm import Session
from app.models.budget import Budget
from app.core.database import SessionLocal
import logging

logger = logging.getLogger(__name__)

class Treasury:
    def __init__(self):
        self.db: Session = SessionLocal()

    def check(self, article: str, amount: float) -> tuple[bool, float]:
        budget = self.db.query(Budget).filter(Budget.article == article).first()
        if not budget:
            return False, 0.0
        available = budget.limit_amount - budget.spent
        if amount > available:
            return False, available
        return True, available - amount

    def commit(self, article: str, amount: float, reason: str, source_agent: str) -> bool:
        budget = self.db.query(Budget).filter(Budget.article == article).first()
        if not budget:
            return False
        budget.spent += amount
        #history record (can be saved in a separate table)
        self.db.commit()
        return True

    def close(self):
        self.db.close()
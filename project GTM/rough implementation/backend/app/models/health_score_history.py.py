from sqlalchemy import Column, Integer, String, Numeric, Date
from app.core.database import Base

class HealthScoreHistory(Base):
    __tablename__ = "health_score_history"

    id = Column(Integer, primary_key=True)
    account_id = Column(String(18), nullable=False)
    date = Column(Date, nullable=False)
    health_score = Column(Numeric(5,2), nullable=False)
    status = Column(String(10))  # green/yellow/red
    created_at = Column(DateTime, server_default=func.now())
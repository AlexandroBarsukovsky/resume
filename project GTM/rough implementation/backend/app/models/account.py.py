from sqlalchemy import Column, String, Numeric, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(String(18), primary_key=True)  # Salesforce ID
    name = Column(String(255), nullable=False)
    account_score = Column(Numeric(5,2), default=0)
    health_score = Column(Numeric(5,2), default=0)
    last_activity = Column(DateTime, nullable=True)
    risk_flag = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
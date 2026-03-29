from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey
from app.core.database import Base

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(String(18), primary_key=True)  # Salesforce ID
    account_id = Column(String(18), ForeignKey("accounts.id"), nullable=False)
    stage = Column(String(50), nullable=False)
    win_probability = Column(Numeric(5,2), default=0)
    amount = Column(Numeric(15,2), nullable=False)
    forecast_category = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
from sqlalchemy import Column, String, Numeric, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Budget(Base):
    __tablename__ = "budget"

    article = Column(String(50), primary_key=True)
    limit_amount = Column(Numeric(10,2), nullable=False)
    spent = Column(Numeric(10,2), default=0)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
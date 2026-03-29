from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(50), primary_key=True)
    subject = Column(String(255), nullable=False)
    description = Column(Text)
    assigned_to = Column(String(255))  # owner ID
    related_to_id = Column(String(18))  # account or opportunity ID
    status = Column(String(20), default="pending")
    priority = Column(String(10), default="normal")
    created_by_agent = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime)
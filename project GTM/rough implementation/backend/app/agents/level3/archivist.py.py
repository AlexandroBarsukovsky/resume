# backend/app/agents/level3/archivist.py
import logging
from sqlalchemy import text
from app.core.database import SessionLocal

logger = logging.getLogger(__name__)

def run(params: dict = None):
    db = SessionLocal()
    try:
        # cleaning old logs
        db.execute(text("DELETE FROM archive_events WHERE created_at < NOW() - INTERVAL '365 days'"))
        db.commit()
    finally:
        db.close()
    logger.info("Archivist run completed")
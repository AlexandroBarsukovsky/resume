# backend/app/agents/level1/intent_monitor.py
from app.services.sixsense import SixSenseClient
from app.services.script1_bridge import publish_task
from app.core.database import SessionLocal
from app.models.account import Account
import logging

logger = logging.getLogger(__name__)

def run(params: dict = None):
    db = SessionLocal()
    sixsense = SixSenseClient()
    try:
        accounts = db.query(Account).all()
        for acc in accounts:
            domain = acc.name  # To put it simply, in reality you need to extract the domain
            intent = sixsense.get_intent(domain)
            if intent > 0.7:
                publish_task(
                    source="intent_monitor",
                    target="account_scorer",
                    payload={"account_id": acc.id, "intent": intent},
                    priority="high"
                )
    finally:
        db.close()
    logger.info("Intent monitor run completed")
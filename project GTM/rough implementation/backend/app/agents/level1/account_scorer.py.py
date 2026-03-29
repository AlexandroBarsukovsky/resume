# backend/app/agents/level1/account_scorer.py
from app.models.ml.account_score import compute_score
from app.services.salesforce import SalesforceClient
from app.services.script1_bridge import publish_task
from app.core.database import SessionLocal
from app.models.account import Account
import logging

logger = logging.getLogger(__name__)

def run(params: dict = None):
    db = SessionLocal()
    sf = SalesforceClient()
    try:
        accounts = db.query(Account).all()
        for acc in accounts:
            # In reality, data is taken from different sources
            intent = 0.5  # placeholder, will be replaced with real data
            usage = 0.6
            icp = 0.8
            score = compute_score(intent, usage, icp)
            acc.account_score = score
            db.commit()
            if score > 0.7:
                publish_task(
                    source="account_scorer",
                    target="task_creator",
                    payload={"account_id": acc.id, "score": score},
                    priority="medium"
                )
    finally:
        db.close()
    logger.info("Account scorer run completed")
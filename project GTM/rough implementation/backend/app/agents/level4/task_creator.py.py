# backend/app/agents/level4/task_creator.py
from app.services.salesforce import SalesforceClient
import logging

logger = logging.getLogger(__name__)

def run(params: dict = None):
    if not params:
        return
    account_id = params.get("account_id")
    score = params.get("score")
    if account_id:
        sf = SalesforceClient()
        sf.create_task(
            subject="Account qualification",
            what_id=account_id,
            owner_id="strategist_queue_id",
            description=f"Account Score {score} exceeded the threshold"
        )
    logger.info("Task creator run completed")
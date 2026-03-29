import logging
from celery import shared_task
from app.services.salesforce import SalesforceClient

logger = logging.getLogger(__name__)

@shared_task
def update_salesforce_task(account_id: str, score: float):
    sf = SalesforceClient()
    sf.update_account_score(account_id, score)
    logger.info(f"Updated Salesforce account {account_id} with score {score}")
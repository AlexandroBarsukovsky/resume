import logging
from celery import shared_task
from app.agents.level1 import intent_monitor, account_scorer
from app.agents.level2 import risk_manager
from app.agents.level4 import forecast_updater

logger = logging.getLogger(__name__)

@shared_task
def update_intent_task():
    logger.info("Updating intent data")
    intent_monitor.run()

@shared_task
def compute_account_score_task():
    logger.info("Computing account scores")
    account_scorer.run()

@shared_task
def compute_health_score_task():
    logger.info("Computing health scores")
    risk_manager.run()

@shared_task
def update_forecast_task():
    logger.info("Updating quarterly forecast")
    forecast_updater.run()
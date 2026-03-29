# backend/app/agents/level4/notification_sender.py
import logging
from app.utils.notifications import send_telegram, send_email

logger = logging.getLogger(__name__)

def run(params: dict = None):
    if params and params.get("account_id"):
        msg = f"Health Score критический для аккаунта {params['account_id']}"
        send_telegram(msg)
        send_email("Health Score Alert", msg)
    logger.info("Notification sender run completed")
import requests
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

def send_telegram(message: str):
    # plug
    logger.info(f"Telegram notification: {message}")

def send_email(subject: str, body: str):
    # plug
    logger.info(f"Email: {subject}")
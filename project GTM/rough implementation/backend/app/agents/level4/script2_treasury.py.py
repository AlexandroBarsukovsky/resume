# backend/app/agents/level4/script2_treasury.py
from app.services.script2_treasury import Treasury
import logging

logger = logging.getLogger(__name__)

def run(params: dict = None):
    treasury = Treasury()
    # periodic budget review
    treasury.close()
    logger.info("Script2 treasury run completed")
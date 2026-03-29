# backend/app/agents/level4/script3_executor.py
from app.services.script3_executor import Executor
import logging

logger = logging.getLogger(__name__)

def run(params: dict = None):
    executor = Executor()
    # for example, starting hightouch sync
    executor.sync_hightouch("sync_id")
    logger.info("Script3 executor run completed")
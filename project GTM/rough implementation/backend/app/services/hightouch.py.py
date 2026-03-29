# backend/app/services/hightouch.py
import requests
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class HightouchClient:
    def __init__(self):
        self.base_url = "https://api.hightouch.com/v1"
        self.api_key = settings.HIGHTOUCH_API_KEY
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def trigger_sync(self, sync_id: str):
        """Start synchronization reverse ETL"""
        url = f"{self.base_url}/syncs/{sync_id}/trigger"
        response = requests.post(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
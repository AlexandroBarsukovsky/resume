# backend/app/services/sixsense.py
import requests
from typing import List, Dict
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class SixSenseClient:
    def __init__(self):
        self.base_url = "https://api.6sense.com/v2"
        self.api_key = settings.SIXSENSE_API_KEY
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_intent(self, account_domain: str) -> float:
        """Get the intent strength for an account (0–1)"""
        url = f"{self.base_url}/companies/{account_domain}/intent"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('intensity', 0.0)
        return 0.0

    def get_bulk_intent(self, domains: List[str]) -> Dict[str, float]:
        """Get an intent for multiple accounts"""
        # simplified, but could actually be a batch API
        result = {}
        for domain in domains:
            result[domain] = self.get_intent(domain)
        return result
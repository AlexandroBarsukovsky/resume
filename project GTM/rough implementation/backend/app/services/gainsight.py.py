# backend/app/services/gainsight.py
import requests
from typing import Dict, Any
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class GainsightClient:
    def __init__(self):
        self.base_url = "https://api.gainsight.com/v1"
        self.api_key = settings.GAINSIGHT_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def update_health_score(self, account_id: str, health_score: float):
        """Refresh Health Score в Gainsight"""
        url = f"{self.base_url}/companies/{account_id}"
        payload = {"custom_fields": {"Health_Score__c": health_score}}
        response = requests.patch(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def trigger_playbook(self, playbook_id: str, account_id: str):
        """Run playbook (hold, expand)"""
        url = f"{self.base_url}/playbooks/{playbook_id}/execute"
        payload = {"companyId": account_id}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()
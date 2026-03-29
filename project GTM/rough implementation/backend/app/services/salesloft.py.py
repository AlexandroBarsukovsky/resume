# backend/app/services/salesloft.py
import requests
from typing import List, Dict
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class SalesLoftClient:
    def __init__(self):
        self.base_url = "https://api.salesloft.com/v2"
        self.api_key = settings.SALESLOFT_API_KEY
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def add_to_cadence(self, person_id: str, cadence_id: str):
        """Add a contact to the calling sequence"""
        url = f"{self.base_url}/cadence_memberships"
        payload = {"cadence_id": cadence_id, "person_id": person_id}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_person(self, email: str, first_name: str, last_name: str, company: str):
        """Create a contact (if not)"""
        url = f"{self.base_url}/persons"
        payload = {
            "email_address": email,
            "first_name": first_name,
            "last_name": last_name,
            "company_name": company
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()
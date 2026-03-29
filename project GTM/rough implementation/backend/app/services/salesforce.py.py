# backend/app/services/salesforce.py
from simple_salesforce import Salesforce
from typing import Dict, List, Optional
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class SalesforceClient:
    def __init__(self):
        self.sf = Salesforce(
            username=settings.SF_USERNAME,
            password=settings.SF_PASSWORD,
            security_token=settings.SF_TOKEN
        )

    def get_accounts_by_score(self, min_score: float = 0.7) -> List[Dict]:
        """Get accounts with an Account Score above the threshold"""
        query = f"SELECT Id, Name, Account_Score__c, Health_Score__c FROM Account WHERE Account_Score__c >= {min_score}"
        result = self.sf.query(query)
        return result.get('records', [])

    def update_account_score(self, account_id: str, score: float):
        """Refresh Account Score в Salesforce"""
        self.sf.Account.update(account_id, {'Account_Score__c': score})

    def update_opportunity_forecast(self, opp_id: str, win_prob: float, forecast_cat: str = None):
        """Update closure probability and forecast category"""
        payload = {'Win_Probability__c': win_prob}
        if forecast_cat:
            payload['Forecast_Category__c'] = forecast_cat
        self.sf.Opportunity.update(opp_id, payload)

    def create_task(self, subject: str, what_id: str, owner_id: str, description: str = None):
        """Create a task in Salesforce"""
        task = {
            'Subject': subject,
            'WhatId': what_id,
            'OwnerId': owner_id,
            'Status': 'Not Started',
            'Priority': 'High'
        }
        if description:
            task['Description'] = description
        return self.sf.Task.create(task)
# backend/app/services/script3_executor.py
from app.services.salesforce import SalesforceClient
from app.services.gainsight import GainsightClient
from app.services.sixsense import SixSenseClient
from app.services.salesloft import SalesLoftClient
from app.services.hightouch import HightouchClient
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self):
        self.sf = SalesforceClient()
        self.gainsight = GainsightClient()
        self.sixsense = SixSenseClient()
        self.salesloft = SalesLoftClient()
        self.hightouch = HightouchClient()

    def update_salesforce_score(self, account_id: str, score: float):
        self.sf.update_account_score(account_id, score)

    def update_opportunity_forecast(self, opp_id: str, win_prob: float):
        self.sf.update_opportunity_forecast(opp_id, win_prob)

    def trigger_retention_playbook(self, account_id: str):
        self.gainsight.trigger_playbook("retention_playbook_id", account_id)

    def sync_hightouch(self, sync_id: str):
        self.hightouch.trigger_sync(sync_id)
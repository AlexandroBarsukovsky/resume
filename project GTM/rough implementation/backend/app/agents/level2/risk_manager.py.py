# backend/app/agents/level2/risk_manager.py
from app.models.ml.health_score import compute_health_score, classify_health_score
from app.core.database import SessionLocal
from app.models.account import Account
from app.models.health_score_history import HealthScoreHistory
from app.services.script1_bridge import publish_task
import logging
from datetime import date

logger = logging.getLogger(__name__)

def run(params: dict = None):
    db = SessionLocal()
    try:
        accounts = db.query(Account).all()
        for acc in accounts:
            # In reality, data is taken from different sources
            deficit = 0.1   # normalized indicators
            turnover = 0.8
            margin = 0.6
            health = compute_health_score(deficit, turnover, margin)
            acc.health_score = health
            status = classify_health_score(health)
            history = HealthScoreHistory(
                account_id=acc.id,
                date=date.today(),
                health_score=health,
                status=status
            )
            db.add(history)
            if health < 0.5:
                publish_task(
                    source="risk_manager",
                    target="notification_sender",
                    payload={"account_id": acc.id, "health_score": health},
                    priority="critical"
                )
        db.commit()
    finally:
        db.close()
    logger.info("Risk manager run completed")
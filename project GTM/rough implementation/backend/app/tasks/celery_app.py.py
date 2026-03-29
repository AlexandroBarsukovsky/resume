from celery import Celery
from celery.schedules import crontab
from app.core.config import settings

celery_app = Celery(
    "sourcegraph_gtm",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["tasks.periodic_tasks", "tasks.agent_tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    broker_connection_retry_on_startup=True,
)

celery_app.conf.beat_schedule = {
    "update_intent_every_30min": {
        "task": "tasks.periodic_tasks.update_intent_task",
        "schedule": crontab(minute="*/30"),
    },
    "compute_account_score_daily": {
        "task": "tasks.periodic_tasks.compute_account_score_task",
        "schedule": crontab(hour=2, minute=0),
    },
    "compute_health_score_daily": {
        "task": "tasks.periodic_tasks.compute_health_score_task",
        "schedule": crontab(hour=3, minute=0),
    },
    "update_forecast_weekly": {
        "task": "tasks.periodic_tasks.update_forecast_task",
        "schedule": crontab(day_of_week=0, hour=23, minute=0),
    },
}
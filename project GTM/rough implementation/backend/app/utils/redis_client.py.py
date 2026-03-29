import redis
import json
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def get_redis():
    return redis_client

def cache_get(key: str):
    return redis_client.get(key)

def cache_set(key: str, value: str, ttl: int = 300):
    redis_client.setex(key, ttl, value)

def publish_event(channel: str, message: dict):
    redis_client.publish(channel, json.dumps(message))
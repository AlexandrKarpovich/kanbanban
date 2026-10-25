import json
import redis.asyncio as redis
from app.config import settings

redis_client: redis.Redis | None = None

async def init_redis() -> None:
    global redis_client
    redis_client = redis.from_url(settings.redis_url, decode_responses=True)

async def close_redis() -> None:
    if redis_client:
        await redis_client.aclose()

async def publish(event: dict) -> None:
    if redis_client is None:
        raise RuntimeError("Redis не инициализирован")
    await redis_client.publish("kanbanban.events", json.dumps(event))
import json
import redis.asyncio as redis
from loguru import logger

redis_client = redis.from_url("redis://localhost:6379")

class NotificationService:
    CHANNEL = "notifications"

    @staticmethod
    async def publish(notification: dict):
        await redis_client.publish(NotificationService.CHANNEL, json.dumps(notification))
        logger.info(f"Published: {notification}")

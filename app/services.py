import json
import redis.asyncio as redis
from loguru import logger

redis_client = redis.from_url("redis://localhost:6379")

class NotificationService:
    CHANNEL = "notifications"

    @staticmethod
    async def publish(notification: dict):
        if notification["broadcast"]:
            await redis_client.publish("broadcast", json.dumps(notification))
        elif notification["topics"]:
            for topic in notification["topics"]:
                await redis_client.publish(f"group:{topic}", json.dumps(notification))
        else:
            for user in notification["recipient_ids"]:
                await redis_client.publish(f"user:{user}", json.dumps(notification))

        logger.info(f"Published: {notification}")

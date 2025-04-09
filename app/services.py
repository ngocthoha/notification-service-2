import json
import redis.asyncio as redis
from loguru import logger

redis_client = redis.from_url("redis://localhost:6379")

class NotificationService:
    CHANNEL = "notifications"

    @staticmethod
    async def publish(notification: dict):
        notif_type = notification["type"]
        target = notification.get("target")
        message = notification["message"]

        channel = {
            "user": f"user:{target}",
            "group": f"group:{target}",
            "broadcast": "broadcast"
        }.get(notif_type)

        if not channel:
            return

        await redis_client.publish(channel, message)
        logger.info(f"Published: {notification}")

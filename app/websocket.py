import json
from .schemas import WebSocketNotification
from .services import redis_client, NotificationService
from loguru import logger
from fastapi import WebSocket


async def redis_listener(channels, websocket: WebSocket):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(*channels)

    async for message in pubsub.listen():
        if message["type"] == "message":
            data = json.loads(message['data'])
            notification = WebSocketNotification(**data)

            await websocket.send_text(notification.message)

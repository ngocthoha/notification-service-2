import json
from .schemas import WebSocketNotification
from .connection import ConnectionManager
from .services import redis_client, NotificationService
from loguru import logger
from fastapi import WebSocket

manager = ConnectionManager()

async def redis_listener(channels, websocket: WebSocket):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(*channels)

    async for message in pubsub.listen():
        if message["type"] == "message":
            await websocket.send_text(message["data"])

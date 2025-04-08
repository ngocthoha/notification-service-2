from fastapi import WebSocket
from collections import defaultdict
from loguru import logger

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}
        self.topics: defaultdict[str, set[str]] = defaultdict(set)

    async def connect(self, websocket: WebSocket, user_id: str, user_topics: list[str]):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        for topic in user_topics:
            self.topics[topic].add(user_id)
        logger.info(f"{user_id} connected with topics: {user_topics}")

    async def disconnect(self, user_id: str):
        websocket = self.active_connections.pop(user_id, None)
        if websocket:
            for users in self.topics.values():
                users.discard(user_id)
            logger.info(f"{user_id} disconnected")

    async def send_personal(self, user_id: str, message: str):
        websocket = self.active_connections.get(user_id)
        if websocket:
            await websocket.send_text(message)
            logger.info(f"Sent personal message to {user_id}")

    async def send_group(self, topic: str, message: str):
        users = self.topics.get(topic, [])
        for user_id in users:
            await self.send_personal(user_id, message)

    async def broadcast(self, message: str):
        for websocket in self.active_connections.values():
            await websocket.send_text(message)
        logger.info("Broadcasted message to all")

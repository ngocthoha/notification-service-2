import json
from .schemas import WebSocketNotification
from .connection import ConnectionManager
from .services import redis_client, NotificationService
from loguru import logger

manager = ConnectionManager()

async def redis_listener():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(NotificationService.CHANNEL)

    async for message in pubsub.listen():
        logger.info(message)
        if message['type'] == 'message':
            data = json.loads(message['data'])
            notification = WebSocketNotification(**data)

            if data.get('broadcast'):
                await manager.broadcast(notification.message)

            if notification.recipient_ids:
                for recipient_id in notification.recipient_ids:
                    await manager.send_personal(recipient_id, notification.message)

            if notification.topics:
                for topic in notification.topics:
                    await manager.send_group(topic, notification.message)

from fastapi import APIRouter
from .schemas import Subscription, NotificationRequest
from .services import NotificationService

router = APIRouter()

user_subscriptions = {}

@router.post("/subscribe")
async def subscribe(subscription: Subscription):
    # Example: You can save subscription info in DB (omitted for simplicity)
    user_id = subscription.user_id
    groups = subscription.topics

    user_subscriptions[user_id] = groups

    return {"status": "subscribed", "user_id": subscription.user_id, "topics": subscription.topics}

@router.post("/send-notification")
async def send_notification(request: NotificationRequest):
    await NotificationService.publish(request.dict())
    return {"status": "notification_sent", "detail": request.dict()}

from typing import List, Optional
from pydantic import BaseModel

class Subscription(BaseModel):
    user_id: str
    topics: List[str]

class NotificationRequest(BaseModel):
    recipient_ids: Optional[List[str]] = None  # Personal
    topics: Optional[List[str]] = None         # Group
    message: str
    broadcast: bool = False                    # Broadcast to all

class WebSocketNotification(BaseModel):
    recipient_ids: Optional[List[str]] = None
    topics: Optional[List[str]] = None
    message: str

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_subscribe():
    response = client.post("/subscribe", json={
        "user_id": "user1",
        "topics": ["topic1", "topic2"]
    })
    assert response.status_code == 200
    assert response.json()["status"] == "subscribed"

@pytest.mark.asyncio
async def test_send_notification():
    response = client.post("/send-notification", json={
        "recipient_ids": ["user1"],
        "message": "Hello user1!"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "notification_sent"

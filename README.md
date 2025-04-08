# Notification Service

A real-time notification microservice built with FastAPI, WebSocket, and Redis pub/sub system. This service enables real-time communication between your application and clients through WebSocket connections, supporting personal, group, and broadcast notifications.

## Features

- Real-time WebSocket notifications
- Redis pub/sub for message distribution
- Multiple notification types:
  - Personal notifications (direct to specific users)
  - Group notifications (via topics)
  - Broadcast notifications (to all connected clients)
- Scalable connection management
- Subscription management for topics

## Prerequisites

- Python 3.8+
- Redis server
- FastAPI
- WebSocket support

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd notification-service
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## API Documentation

### REST Endpoints

#### 1. Subscribe to Topics
```http
POST /subscribe
```
Subscribe a user to specific topics.

Request body:
```json
{
    "user_id": "string",
    "topics": ["string"]
}
```
Response:
```json
{
    "status": "subscribed",
    "user_id": "string",
    "topics": ["string"]
}
```

#### 2. Send Notification
```http
POST /send-notification
```
Send a notification to specific users, topics, or broadcast to all.

Request body:
```json
{
    "recipient_ids": ["string"],  // Optional: List of user IDs for personal notifications
    "topics": ["string"],         // Optional: List of topics for group notifications
    "message": "string",          // Required: The notification message
    "broadcast": false           // Optional: Set to true for broadcast to all
}
```
Response:
```json
{
    "status": "notification_sent",
    "detail": {
        // Request details
    }
}
```

### WebSocket Endpoint

#### Connect to WebSocket
```http
GET /ws/notifications
```
Establish a WebSocket connection for real-time notifications.

Example JavaScript client:
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/notifications?user_id=user123&topics=topic1,topic2');

ws.onmessage = function(event) {
    const notification = JSON.parse(event.data);
    console.log('Received notification:', notification);
};

ws.onopen = function() {
    console.log('Connected to notification service');
};

ws.onclose = function() {
    console.log('Disconnected from notification service');
};
```

## Notification Types

1. **Personal Notifications**
   - Sent to specific users using their `recipient_ids`
   - Delivered only to the specified users

2. **Group Notifications**
   - Sent to all users subscribed to specific topics
   - Use the `topics` field to specify target groups

3. **Broadcast Notifications**
   - Sent to all connected clients
   - Set `broadcast: true` in the request

## Development

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Run tests:
```bash
pytest
```

3. Start the development server:
```bash
uvicorn app.main:app --reload
```

## Configuration

The service can be configured through environment variables:

- `REDIS_HOST`: Redis server host (default: localhost)
- `REDIS_PORT`: Redis server port (default: 6379)
- `REDIS_DB`: Redis database number (default: 0)
- `REDIS_PASSWORD`: Redis password (if required)

## Error Handling

The service includes comprehensive error handling for:
- Invalid WebSocket connections
- Redis connection issues
- Invalid notification formats
- Missing required fields

## License

[Your License]

## Contributing

[Your Contributing Guidelines]
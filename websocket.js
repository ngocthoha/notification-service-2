const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:8000/ws/notifications?user_id=user123&topics=topic1,topic2');

ws.on('open', () => {
  console.log('WebSocket connected');
});

ws.on('message', (message) => {
  console.log('Received:', message.toString());
});

ws.on('close', () => {
  console.log('WebSocket disconnected');
});

ws.on('error', (error) => {
  console.error('WebSocket Error:', error);
});

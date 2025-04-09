from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
import asyncio
from contextlib import asynccontextmanager
from loguru import logger
from .connection import manager
from .api import router as api_router
from .websocket import redis_listener




# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     asyncio.create_task(redis_listener())
#     yield

app = FastAPI()
app.include_router(api_router)

@app.websocket("/ws/notifications")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: str = Query(...),
    topics: str = Query("")
):
    user_topics = topics.split(",") if topics else []
    await manager.connect(websocket, user_id, user_topics)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await manager.disconnect(user_id)

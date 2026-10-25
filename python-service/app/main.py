import asyncio
import contextlib
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.config import settings
from app.grpc.server import start_grpc_server
from app.redis.pubsub import close_redis, init_redis

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Подключаем Redis при старте
    await init_redis()
    print("✅ Redis успешно подключен")
    yield
    # Отключаем при выключении
    await close_redis()
    print("Соединение с Redis закрыто")

app = FastAPI(title=settings.app_name, lifespan=lifespan)

@app.get("/health")
async def health():
    return {"status": "ok"}

async def run_all():
    # 1. Запускаем gRPC
    grpc_server = await start_grpc_server(settings.grpc_port)
    print(f"✅ gRPC сервер слушает порт {settings.grpc_port}")

    # 2. Запускаем FastAPI (HTTP)
    config = uvicorn.Config(app, host="0.0.0.0", port=settings.http_port, log_level="info")
    http_server = uvicorn.Server(config)
    print(f"✅ FastAPI слушает порт {settings.http_port}")

    # 3. Держим оба сервера включенными
    with contextlib.suppress(asyncio.CancelledError):
        await asyncio.gather(
            grpc_server.wait_for_termination(),
            http_server.serve()
        )

if __name__ == "__main__":
    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
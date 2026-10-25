from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings

# Движок (engine) — это пул соединений с базой данных. Создается один раз при старте.
engine = create_async_engine(settings.database_url, echo=False)

# Фабрика сессий. Каждый запрос к базе данных будет использовать свою сессию.
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
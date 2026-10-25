from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Говорим Pydantic искать файл .env в корне проекта
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Описываем переменные, которые ожидаем найти в .env
    app_name: str = "KanBanBan Python Service"
    grpc_port: int = 50051
    http_port: int = 8000

    # Обязательные переменные (без значений по умолчанию)
    database_url: str
    redis_url: str


# Создаем экземпляр, который будем импортировать везде
settings = Settings()
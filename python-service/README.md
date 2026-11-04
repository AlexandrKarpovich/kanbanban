# KanBanBan: Python Domain Service

Этот микросервис является ядром приложения KanBanBan. 
Он отвечает за бизнес-логику, хранение данных в PostgreSQL и публикацию событий в Redis.

## 🛠 Стек
- Python 3.15
- FastAPI (HTTP-слой для health-check и отладки)
- gRPC (для общения с Node.js BFF)
- SQLAlchemy 2.0 + asyncpg (асинхронная работа с БД)
- Alembic (миграции)
- Redis (Pub/Sub для WebSockets)

## 🚀 Быстрый старт (локальная разработка)

1. Создайте и активируйте виртуальное окружение:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
Установите зависимости:

powershell
pip install -r requirements.txt
Скопируйте настройки окружения:

powershell
Copy-Item .env.example .env
Запустите сервис:

powershell
python -m app.main
🔄 Генерация gRPC-кода
Если вы изменили контракты в папке proto/, вам нужно сгенерировать Python-код заново. Выполните команду из корня python-service:

powershell
python -m grpc_tools.protoc -Iproto --python_out=app/grpc --grpc_python_out=app/grpc proto/имя_файла.proto


запустить бд
docker start kanban-postgres
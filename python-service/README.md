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

```text
python-service/
├── app/
│   ├── main.py              # Точка входа: запускает FastAPI и gRPC одновременно
│   ├── config.py            # Чтение настроек из .env (Pydantic Settings)
│   ├── db/
│   │   ├── session.py       # Настройка асинхронного подключения к PostgreSQL (engine, sessionmaker)
│   │   └── base.py          # Базовый класс Base для всех моделей SQLAlchemy
│   ├── models/              # SQLAlchemy модели (таблицы БД: User, Board, Task и т.д.)
│   ├── grpc/
│   │   ├── server.py        # Инициализация и запуск gRPC-сервера
│   │   └── services/        # Реализация gRPC-методов (бизнес-логика)
│   └── redis/
│       └── pubsub.py        # Клиент для отправки событий (например, 'task.moved') в Redis
├── proto/                   # .proto файлы (контракты gRPC)
│   └── health.proto         # Пример минимального сервиса для проверки связи
├── alembic/                 # Скрипты миграций базы данных
├── alembic.ini              # Конфигурация Alembic
├── requirements.txt         # Список зависимостей Python
├── .env.example             # Шаблон переменных окружения (для git)
└── .env                     # Твои локальные секреты (в git не попадает)
```

## 🔄 Генерация gRPC-кода

Если вы изменили контракты в папке `proto/`, вам нужно сгенерировать Python-код заново. Выполните команду из корня `python-service`:

```powershell
python -m grpc_tools.protoc -Iproto --python_out=app/grpc --grpc_python_out=app/grpc proto/имя_файла.proto
```
Примечание: после генерации не забудьте проверить импорты в файлах *_pb2_grpc.py (они должны начинаться с from app.grpc import ...).

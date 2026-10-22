
# 🐗 KanBanBan

> Канбан-доска для команд. Канбан + Кабан = порядок в задачах.

**KanBanBan** — лёгкая альтернатива Trello для небольших команд. Построена на микросервисной архитектуре с gRPC и WebSocket — потому что кабан не терпит тормозов.

Проект сфокусирован на **бэкенде**: микросервисы, gRPC-контракты, real-time через WebSocket, работа с PostgreSQL и Redis. Фронт — витрина для демонстрации API.


## 🏗️ Архитектура

```text
[ Python Service ] --( gRPC )--> [ Node.js BFF ] --( REST + WS )--> [ React App ]
        |                               |
        |                               |
        +-------( Redis Pub/Sub )-------+
        |
        v
[ PostgreSQL ]

---

- **Python Service** — доменная логика, gRPC-сервер, работа с БД.
- **Node.js BFF** — API Gateway под фронт: REST + WebSocket, агрегирует данные из Python.
- **Redis Pub/Sub** — мост между Python и Node для real-time событий.
- **PostgreSQL** — основное хранилище.
- **React** — фронт, общается только с BFF.

---

## 🛠️ Стек

| Слой | Технология |
|---|---|
| Доменный сервис | Python 3.12 + FastAPI + grpcio + SQLAlchemy + Alembic |
| BFF | Node.js + NestJS + socket.io + @grpc/grpc-js |
| БД | PostgreSQL + Redis |
| Контракты | Protocol Buffers (gRPC) |
| Инфраструктура | Docker + Docker Compose |
| Деплой | Railway (бэк), Vercel (фронт) |
| Фронт | React + TypeScript + Vite + dnd-kit |

---

## ⚙️ Бэкенд: возможности

- 🔐 Регистрация и авторизация (JWT)
- 📋 CRUD досок, колонок, задач
- 👥 Назначение исполнителей
- 💬 Комментарии к задачам
- ⚡ Real-time синхронизация через WebSocket
- 🔔 Мгновенные уведомления о событиях
- 🔎 Фильтры по исполнителю и статусу
- 🧵 Асинхронность: `asyncio` + `asyncpg`
- 📡 gRPC между сервисами
- 📨 Redis Pub/Sub для событий

---

## 📁 Структура репозитория

```text
kanbanban/
├── proto/              # .proto файлы (общие контракты)
├── python-service/     # FastAPI + gRPC
├── node-bff/           # NestJS + WebSocket + gRPC-клиент
├── react-app/          # React + TS
├── docker-compose.yml  # Локальный запуск
└── README.md
```

---

## ⚙️ Локальный запуск

### Требования
- Docker + Docker Compose
- Python 3.12+
- Node.js 20+

### 1. Клонировать репозиторий
```bash
git clone https://github.com/your-username/kanbanban.git
cd kanbanban
```

### 2. Поднять инфраструктуру
```bash
docker compose up -d postgres redis
```

### 3. Запустить Python-сервис
```bash
cd python-service
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

### 4. Запустить Node BFF
```bash
cd node-bff
npm install
npm run start:dev
```

### 5. Запустить фронт
```bash
cd react-app
npm install
npm run dev
```

Открыть: http://localhost:5173

---

## 🌐 Деплой

| Компонент | Платформа | URL |
|---|---|---|
| Python Service | Railway | приватный домен |
| Node BFF | Railway | `kanbanban-bff.up.railway.app` |
| PostgreSQL | Railway | managed |
| Redis | Railway | managed |
| React | Vercel | `kanbanban.vercel.app` |

---

## 🖥️ Фронт: возможности

- 🖱️ Drag-and-drop задач между колонками
- ⚡ Real-time обновления доски
- 🔔 Живые уведомления
- 🔐 Авторизация через JWT

---

## 🐗 Почему «KanBanBan»?

**KanBan** + **КаBan** = **Кабан**. Кабан — упёртый, пробивной, разгребает любые задачи. Как твой бэклог в понедельник утром.

---

## 📸 Скриншоты

*(добавить позже)*

---

## 📝 Лицензия

MIT — делай что хочешь, только кабана не обижай.
```
**До сюда**.

После вставки обязательно нажми "Commit changes".
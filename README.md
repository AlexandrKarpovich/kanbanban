# 🐗 KanBanBan

> Канбан-доска для команд. Канбан + Кабан = порядок в задачах.

**KanBanBan** — лёгкая альтернатива Trello для небольших команд. Построена на микросервисной архитектуре с gRPC и WebSocket — потому что кабан не терпит тормозов.

Проект сфокусирован на **бэкенде**: микросервисы, gRPC-контракты, real-time через WebSocket, работа с PostgreSQL и Redis. Фронт — витрина для демонстрации API.

---

## 🏗️ Архитектура

```
┌──────────────┐   gRPC   ┌──────────────┐   REST + WS   ┌─────────────┐
│ Java Service │ ───────► │  Node.js BFF │ ────────────► │   React     │
│  (Railway)   │ ◄─────── │  (Railway)   │ ◄──────────── │  (Vercel)   │
└──────┬───────┘          └──────┬───────┘               └─────────────┘
       │                         │
       │  Redis Pub/Sub          │
       └──────────┬──────────────┘
                  ▼
       ┌──────────────────────┐
       │ PostgreSQL + Redis   │
       └──────────────────────┘
```

- **Java Service** — доменная логика, gRPC-сервер, работа с БД.
- **Node.js BFF** — API Gateway под фронт: REST + WebSocket, агрегирует данные из Java.
- **Redis Pub/Sub** — мост между Java и Node для real-time событий.
- **PostgreSQL** — основное хранилище.
- **React** — фронт, общается только с BFF.

---

## 🛠️ Стек

| Слой | Технология |
|---|---|
| Доменный сервис | Java 21 + Spring Boot 3 + grpc-spring-boot-starter |
| BFF | Node.js + NestJS + socket.io |
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
- 🧵 Многопоточность: `@Async` + `CompletableFuture`
- 📡 gRPC между сервисами
- 📨 Redis Pub/Sub для событий

---

## 📁 Структура репозитория

```
kanbanban/
├── proto/              # .proto файлы (общие контракты)
├── java-service/       # Spring Boot + gRPC
├── node-bff/           # NestJS + WebSocket + gRPC-клиент
├── react-app/          # React + TS
├── docker-compose.yml  # Локальный запуск
└── README.md
```

---

## ⚙️ Локальный запуск

### Требования
- Docker + Docker Compose
- Java 21
- Maven
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

### 3. Запустить Java-сервис
```bash
cd java-service
./mvnw spring-boot:run
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
| Java Service | Railway | приватный домен |
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
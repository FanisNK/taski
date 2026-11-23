# Taski

Приложение для удобного планирования и отслеживания повседневных задач. Позволяет создавать, редактировать, удалять задачи, отмечать их выполненными и управлять списком дел через REST API.

## Возможности

- Создание новых задач.
- Редактирование существующих задач.
- Удаление задач.
- Отметка задач как выполненных.
- Просмотр списка активных и выполненных задач.
- REST API для управления задачами.
- Возможность создавать задачи без описания.

## Стек технологий

### Backend
- Python
- Django
- Django REST Framework
- SQLite

### Frontend
- React
- JavaScript
- Axios
- Reactstrap

### Инструменты
- Git
- GitHub
- npm

## Как запустить проект локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/FanisNK/taski.git
cd taski
```

### 2. Настроить backend

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать файл `.env` в корне проекта на основе `.env.example` и заполнить необходимые переменные окружения.

Выполнить миграции:

```bash
python backend/manage.py migrate
```

Запустить Django:

```bash
python backend/manage.py runserver
```

Backend будет доступен по адресу `http://127.0.0.1:8000/`.

### 3. Настроить frontend

Перейти в папку frontend:

```bash
cd frontend
```

Установить зависимости:

```bash
npm install
```

Запустить React:

```bash
npm start
```

Frontend будет доступен по адресу `http://localhost:3000/`.

## API

API предоставляет возможность управлять задачами.

| Метод | Endpoint | Описание |
|---|---|---|
| GET | `/api/tasks/` | Получить список задач |
| POST | `/api/tasks/` | Создать задачу |
| GET | `/api/tasks/{id}/` | Получить конкретную задачу |
| PUT | `/api/tasks/{id}/` | Обновить задачу |
| PATCH | `/api/tasks/{id}/` | Частично обновить задачу |
| DELETE | `/api/tasks/{id}/` | Удалить задачу |

### Пример создания задачи

```json
{
  "title": "Изучить Django",
  "description": "Разобраться с REST API",
  "completed": false
}
```

### Формат задачи

```json
{
  "id": 1,
  "title": "Изучить Django",
  "description": "Разобраться с REST API",
  "completed": false
}
```

## Контакты

- GitHub: [FanisNK](https://github.com/FanisNK)
- Telegram: @fanis777

## Лицензия

Проект распространяется под лицензией MIT.

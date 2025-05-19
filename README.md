# 🚀 FastAPI Blog

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

Проект для создания личных блогов с использованием современного стека технологий.

## 🛠️ Технологический стек

### Основные технологии
- **Python 3.13+**: Современная версия языка программирования
- **FastAPI 0.115+**: Высокопроизводительный веб-фреймворк для создания API
- **SQLAlchemy 2.0+**: ORM для работы с базами данных
- **Pydantic**: Валидация данных и сериализация
- **PostgreSQL**: Основная база данных (через asyncpg)

### Инструменты разработки
- **Docker & Docker Compose**: Контейнеризация и оркестрация
- **Alembic**: Миграции базы данных
- **pytest**: Тестирование
- **ruff**: Линтер и форматер кода
- **mypy**: Статический анализатор типов
- **pre-commit**: Автоматизация проверок перед коммитом

## 🏗️ Архитектура проекта
Проект следует принципам чистой архитектуры:
- Роутеры (API endpoints)
- Сервисный слой (бизнес-логика)
- Репозитории (работа с БД)
- Модели данных (SQLAlchemy)
- Схемы (Pydantic)

## 📦 Быстрый старт

1. **Клонирование репозитория:**
```bash
git clone https://github.com/macalistervadim/fastapi-blog
cd fastapi-blog
```

2. **Настройка окружения:**
```bash
cp .env.example .env.local
```
3. **Запуск проекта:**
```bash
docker-compose -f docker-compose.local.yml up -d
```

4. **Создание миграций:**
```bash
docker-compose -f docker-compose.local.yml exec web alembic revision --autogenerate -m "Initial migration"
```
   
5. **Применение миграций:**
```bash
docker-compose -f docker-compose.local.yml exec web alembic upgrade head
```
   
6. **Проверка работоспособности:**
Откройте браузер и перейдите по адресу [http://localhost:8000/docs](http://localhost:8000/docs) для доступа к Swagger UI.

P.S - Данная инструкция предусматривает, что вы опытный пользователь используемых в проекте инструментов и не включает в себя подробные шаги по установке и настройке Docker, Docker Compose, виртуального окружения и других инструментов. Если у вас возникли трудности, пожалуйста, обратитесь к официальной документации.

## 🧪 Тестирование
Для запуска тестов используйте команду:
```bash
docker-compose -f docker-compose.local.yml exec web pytest
```

## 📜 Лицензия
Этот проект лицензирован под MIT License. Пожалуйста, ознакомьтесь с файлом [LICENSE](LICENSE) для получения подробной информации.

## 📫 Контакты
Вопросы и предложения принимаются в [issue](https://github.com/macalistervadim/fastapi-blog/issues)
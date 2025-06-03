# Проект самообучения

## Описание

Этот проект представляет собой веб-приложение на Django, предназначенное для организации процесса самообучения. Проект включает в себя систему пользователей и управление материалами для обучения.

## Технологии

- Python 3.x
- Django 5.2.1
- Django REST Framework 3.16.0
- PostgreSQL
- Pillow 11.2.1
- python-dotenv 1.1.0

## Установка и настройка

1. Клонируйте репозиторий:

```bash
git clone <url-репозитория>
cd coursework
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта и добавьте следующие переменные окружения:

```
USER_POSTGRES=your_postgres_user
USER_PASSWORD=your_postgres_password
EMAIL_HOST_USER=your_email@yandex.ru
EMAIL_HOST_PASSWORD=your_email_password
```

5. Создайте базу данных PostgreSQL с именем 'self_study'

6. Примените миграции:

```bash
python manage.py migrate
```

7. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

8. Запустите сервер разработки:

```bash
python manage.py runserver
```

## Структура проекта

- `coursework/` - основные настройки проекта
- `users/` - приложение для управления пользователями
- `materials/` - приложение для управления учебными материалами
- `templates/` - HTML шаблоны
- `static/` - статические файлы (CSS, JavaScript, изображения)
- `media/` - загруженные пользователями файлы

## Функциональность

- Система аутентификации и авторизации пользователей
- Управление профилем пользователя
- Загрузка и управление учебными материалами
- REST API для взаимодействия с данными
- Подтверждение email при регистрации

## API Endpoints

API документация доступна по адресу `/api/docs/` после запуска сервера.
# Локальный запуск (Quick Start)

## 1. Переключиться на ветку разработки

```bash
git fetch origin
git checkout django-development
git pull origin django-development
```

## 2. Окружение

```bash
# Создать виртуальное окружение
python -m venv venv

# Активировать (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Установить зависимости
pip install -r requirements.txt
```

## 3. Переменные окружения

Файл `.env` уже содержит:
- `DEBUG=True` — для локальной разработки
- `SECRET_KEY` — ключ Django

При необходимости добавить `DATABASE_URL` для PostgreSQL (по умолчанию используется SQLite).

## 4. База данных и данные

```bash
python manage.py migrate
python manage.py create_initial_data
python manage.py loaddata all_data
```

## 5. Админка — создать дефолтного администратора

```bash
python manage.py create_default_admin
```

**Логин:** `admin`  
**Пароль:** `admin123`  
**Админка:** http://127.0.0.1:8000/admin/

Кастомные учётные данные (опционально):

```bash
python manage.py create_default_admin --username myadmin --password mypass
```

## 6. Запуск сервера

```bash
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/

## Полезные URL

| Страница      | URL                         |
|---------------|-----------------------------|
| Главная       | http://127.0.0.1:8000/      |
| Обучение      | http://127.0.0.1:8000/training/ |
| Инструкции    | http://127.0.0.1:8000/instructions/ |
| О кофе        | http://127.0.0.1:8000/coffee-info/ |
| Ценности      | http://127.0.0.1:8000/business-values/ |
| Админка       | http://127.0.0.1:8000/admin/ |

## Проверка данных

```bash
python scripts/check_data.py
```

---

## Railway — деплой

При деплое `create_default_admin` выполняется автоматически.

**Важно для продакшена:** задайте в Railway переменные окружения:
- `ADMIN_PASSWORD` — пароль для админа (обязательно!)
- `ADMIN_USERNAME` — логин (по умолчанию: admin)
- `ADMIN_EMAIL` — email (по умолчанию: admin@dimkava.local)
- `DEBUG=False`
- `SECRET_KEY` — свой ключ (или оставить из .env)
- `DATABASE_URL` — Railway добавляет автоматически

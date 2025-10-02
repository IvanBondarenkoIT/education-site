# 🚀 ПЛАН ДЕПЛОЯ НА HEROKU (БЕСПЛАТНЫЙ ПЛАН)

## 📋 ОБЗОР ПЛАНА

### Цель:
Деплой Django сайта "Dim Kava" на Heroku для тестирования операторами

### Платформа:
- **Heroku** (бесплатный план)
- **PostgreSQL** (бесплатная база данных)
- **Whitenoise** (для статических файлов)

### Ограничения бесплатного плана:
- 512MB RAM
- 30 минут сна в день
- 550-1000 часов в месяц
- PostgreSQL 10MB

## 🔧 ПОДГОТОВКА ПРОЕКТА

### 1. Обновление requirements.txt
```bash
# Добавить необходимые пакеты для Heroku
pip install whitenoise gunicorn psycopg2-binary dj-database-url
pip freeze > requirements.txt
```

### 2. Создание файлов для Heroku

#### Procfile
```
web: gunicorn education_site.wsgi --log-file -
```

#### runtime.txt
```
python-3.11.7
```

### 3. Обновление settings.py
```python
import os
import dj_database_url
from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-wf3ooiv&h557s=gge(d7lj1-hmjkubdnigq=9qocpsu3v_v%(_')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '.herokuapp.com']

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware для статических файлов
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Добавить в начало
    # ... остальные middleware
]
```

## 🚀 ПРОЦЕСС ДЕПЛОЯ

### 1. Установка Heroku CLI
```bash
# Windows
winget install --id=Heroku.HerokuCLI

# Или скачать с https://devcenter.heroku.com/articles/heroku-cli
```

### 2. Логин в Heroku
```bash
heroku login
```

### 3. Создание приложения
```bash
heroku create dom-kofe-education
```

### 4. Настройка переменных окружения
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set DJANGO_SETTINGS_MODULE=education_site.settings
```

### 5. Добавление PostgreSQL
```bash
heroku addons:create heroku-postgresql:mini
```

### 6. Деплой
```bash
git add .
git commit -m "Heroku deployment setup"
git push heroku main
```

### 7. Миграции и импорт данных
```bash
heroku run python manage.py migrate
heroku run python manage.py import_training_program
heroku run python manage.py import_job_instructions
heroku run python manage.py import_coffee_info
```

## 📁 СТРУКТУРА ФАЙЛОВ ДЛЯ HEROKU

```
project/
├── Procfile                    # Команда запуска
├── runtime.txt                 # Версия Python
├── requirements.txt            # Зависимости
├── education_site/
│   ├── settings.py            # Обновленные настройки
│   └── wsgi.py                # WSGI приложение
├── core/                       # Django приложение
├── templates/                  # Шаблоны
├── static/                     # Статические файлы
└── docs/                       # Документация
```

## 🔧 НЕОБХОДИМЫЕ ИЗМЕНЕНИЯ

### 1. Обновить requirements.txt
```
asgiref==3.9.1
beautifulsoup4==4.13.4
Django==5.2.5
django-ckeditor==6.7.3
django-crispy-forms==2.4
django-js-asset==3.1.2
django-modeltranslation==0.19.16
dj-database-url==2.1.0
gunicorn==21.2.0
pillow==11.3.0
psycopg2-binary==2.9.9
soupsieve==2.7
sqlparse==0.5.3
typing_extensions==4.14.1
tzdata==2025.2
whitenoise==6.6.0
```

### 2. Создать Procfile
```
web: gunicorn education_site.wsgi --log-file -
```

### 3. Создать runtime.txt
```
python-3.11.7
```

### 4. Обновить settings.py
- Добавить поддержку переменных окружения
- Настроить PostgreSQL
- Добавить Whitenoise для статических файлов
- Обновить ALLOWED_HOSTS

## 🚨 ВОЗМОЖНЫЕ ПРОБЛЕМЫ И РЕШЕНИЯ

### 1. Статические файлы
**Проблема:** Heroku не обслуживает статические файлы
**Решение:** Использовать Whitenoise

### 2. База данных
**Проблема:** SQLite не работает на Heroku
**Решение:** Использовать PostgreSQL

### 3. Секретный ключ
**Проблема:** Секретный ключ в коде
**Решение:** Использовать переменные окружения

### 4. Отладка
**Проблема:** DEBUG=True в продакшене
**Решение:** Установить DEBUG=False

## 📊 МОНИТОРИНГ И ЛОГИ

### Просмотр логов
```bash
heroku logs --tail
```

### Мониторинг ресурсов
```bash
heroku ps
heroku addons
```

### Перезапуск приложения
```bash
heroku restart
```

## 🔒 БЕЗОПАСНОСТЬ

### Переменные окружения
- SECRET_KEY
- DATABASE_URL (автоматически)
- DEBUG=False

### Настройки безопасности
- DEBUG=False в продакшене
- HTTPS только
- Безопасные заголовки

## 📱 ТЕСТИРОВАНИЕ ОПЕРАТОРАМИ

### URL для тестирования
```
https://dom-kofe-education.herokuapp.com
```

### Функции для тестирования
1. **Многоязычность** (ru, uk, en, ge)
2. **Программа обучения**
3. **Должностные инструкции**
4. **Информация о кофе**
5. **Ценности компании**

### Ограничения для тестирования
- 30 минут сна в день
- Медленная загрузка при пробуждении
- Ограниченная база данных (10MB)

## 💰 СТОИМОСТЬ

### Бесплатный план:
- ✅ Приложение: $0/месяц
- ✅ PostgreSQL: $0/месяц
- ✅ SSL: $0/месяц
- ✅ Домен: $0/месяц

### Ограничения:
- ❌ 512MB RAM
- ❌ 30 минут сна
- ❌ 550-1000 часов/месяц
- ❌ PostgreSQL 10MB

## 🎯 СЛЕДУЮЩИЕ ШАГИ

### После деплоя:
1. **Тестирование функциональности**
2. **Проверка многоязычности**
3. **Тестирование импорта данных**
4. **Мониторинг производительности**

### При необходимости масштабирования:
1. **Переход на платный план**
2. **Увеличение ресурсов**
3. **Настройка CDN**
4. **Оптимизация базы данных**

---

**Статус:** План готов к реализации  
**Сложность:** Средняя  
**Время реализации:** 2-4 часа  
**Стоимость:** $0/месяц








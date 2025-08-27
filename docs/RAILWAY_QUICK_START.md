# 🚂 БЫСТРЫЙ ДЕПЛОЙ НА RAILWAY (10 МИНУТ)

## 🎯 Почему Railway?

- ✅ **Самый простой деплой** - подключил GitHub и готово
- ✅ **Бесплатно навсегда** - 500 часов в месяц
- ✅ **Автоматический SSL** и домен
- ✅ **PostgreSQL** включен в бесплатный план
- ✅ **Автоматические деплои** при push в Git

## 🚀 Пошаговая инструкция

### Шаг 1: Подготовка проекта

1. **Убедитесь, что проект в GitHub**
2. **Проверьте requirements.txt:**
   ```txt
   Django==5.2.5
   gunicorn==23.0.0
   psycopg2-binary==2.9.10
   whitenoise==6.9.0
   # ... остальные зависимости
   ```

### Шаг 2: Регистрация на Railway

1. **Перейдите на:** https://railway.app/
2. **Нажмите "Start a New Project"**
3. **Войдите через GitHub**
4. **Разрешите доступ к репозиториям**

### Шаг 3: Создание проекта

1. **Выберите "Deploy from GitHub repo"**
2. **Найдите ваш репозиторий** `education-site`
3. **Нажмите "Deploy Now"**

### Шаг 4: Настройка базы данных

1. **В проекте нажмите "New"**
2. **Выберите "Database" > "PostgreSQL"**
3. **Railway автоматически создаст базу данных**

### Шаг 5: Настройка переменных окружения

1. **Перейдите в настройки веб-сервиса**
2. **Добавьте переменные:**
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://... (автоматически)
   ```

### Шаг 6: Деплой

1. **Railway автоматически деплоит приложение**
2. **Получите URL:** `https://your-app.railway.app`
3. **Приложение готово!**

## 🔧 Настройка Django для Railway

### 1. Обновите requirements.txt:
```txt
Django==5.2.5
gunicorn==23.0.0
psycopg2-binary==2.9.10
whitenoise==6.9.0
dj-database-url==3.0.1
```

### 2. Создайте Procfile:
```
web: gunicorn education_site.wsgi --log-file -
```

### 3. Обновите settings.py:
```python
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.railway.app']

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

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Добавить
    # ... остальные middleware
]
```

## 📊 Проверка деплоя

### 1. Откройте URL приложения
### 2. Проверьте все страницы:
- ✅ Главная страница
- ✅ Программа обучения
- ✅ Должностные инструкции
- ✅ Информация о кофе
- ✅ Бизнес-ценности

### 3. Проверьте многоязычность:
- ✅ Переключение языков
- ✅ Контент на всех языках

## 🚨 Решение проблем

### Проблема: "Build failed"
**Решение:**
1. Проверьте requirements.txt
2. Убедитесь, что все зависимости указаны
3. Проверьте логи в Railway

### Проблема: "Application Error"
**Решение:**
1. Проверьте переменные окружения
2. Убедитесь, что DEBUG=False
3. Проверьте логи приложения

### Проблема: Статические файлы не загружаются
**Решение:**
1. Добавьте whitenoise в middleware
2. Настройте STATICFILES_STORAGE
3. Соберите статические файлы

## 📈 Мониторинг

### В Railway Dashboard:
- 📊 **Использование ресурсов**
- 📝 **Логи приложения**
- 🔄 **История деплоев**
- ⚙️ **Настройки**

### Полезные команды:
```bash
# Локальная проверка
python manage.py check --deploy

# Сбор статических файлов
python manage.py collectstatic --noinput

# Проверка миграций
python manage.py showmigrations
```

## 🎯 Результат

После успешного деплоя:
- 🌐 **URL:** `https://your-app.railway.app`
- 📱 **Доступно операторам** для тестирования
- 🔄 **Автоматические обновления** при push в Git
- 🔒 **SSL сертификат** включен
- 🗄️ **PostgreSQL база данных** работает

## 💰 Стоимость

- **Бесплатно:** 500 часов в месяц
- **Платно:** $5/месяц за 1000 часов
- **База данных:** Включена в бесплатный план

---

**Время деплоя:** 10-15 минут  
**Сложность:** Очень простая  
**Стоимость:** $0/месяц  
**Статус:** Готов к использованию! 🚀

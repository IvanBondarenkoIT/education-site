# 🚀 ИНСТРУКЦИИ ПО ЗАПУСКУ ПРОЕКТА

## 📋 Предварительные требования

### Системные требования:
- **OS:** Windows 10/11, Linux, macOS
- **Python:** 3.8 или выше
- **Git:** для работы с репозиторием

### Проверка Python:
```bash
python --version
# Должно быть: Python 3.8.x или выше
```

## 🏗️ Первоначальная настройка

### 1. Клонирование/скачивание проекта
```bash
# Если проект уже скачан, переходим к следующему шагу
cd "D:\Education Site"
```

### 2. Активация виртуального окружения

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```

## 🚀 Запуск проекта

### 1. Активация окружения
```bash
cd "D:\Education Site"
.\venv\Scripts\activate
```

### 2. Проверка данных
```bash
python scripts/check_data.py
```

**Ожидаемый результат:**
```
📊 BusinessValue: 33 записей
📚 TrainingProgram: 8 записей
👔 JobInstruction: 9 записей
☕ CoffeeInfo: 5 записей
```

### 3. Запуск сервера разработки
```bash
python manage.py runserver
```

### 4. Открытие в браузере
- **Главная страница:** http://127.0.0.1:8000/
- **Админка:** http://127.0.0.1:8000/admin/

## 🔧 Полезные команды

### Проверка состояния проекта
```bash
# Проверка данных в БД
python scripts/check_data.py

# Проверка версии Django
python -c "import django; print(django.get_version())"

# Проверка установленных пакетов
pip list
```

### Работа с данными
```bash
# Импорт данных (если нужно)
python manage.py import_training_program
python manage.py import_job_instructions
python manage.py import_coffee_info

# Очистка данных (если нужно)
python manage.py clear_incorrect_data --confirm
```

### Миграции
```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Просмотр статуса миграций
python manage.py showmigrations
```

### Статические файлы
```bash
# Сбор статических файлов
python manage.py collectstatic
```

## 🌐 Доступные URL

После запуска сервера доступны следующие страницы:

| URL | Описание |
|-----|----------|
| http://127.0.0.1:8000/ | Главная страница |
| http://127.0.0.1:8000/training/ | Программа обучения |
| http://127.0.0.1:8000/instructions/ | Должностные инструкции |
| http://127.0.0.1:8000/coffee-info/ | Информация о кофе |
| http://127.0.0.1:8000/business-values/ | Бизнес-ценности |
| http://127.0.0.1:8000/admin/ | Административная панель |

## 🚨 Решение проблем

### Проблема: "No module named 'django'"
**Решение:** Убедитесь, что виртуальное окружение активировано
```bash
.\venv\Scripts\activate
```

### Проблема: "Port 8000 is already in use"
**Решение:** Используйте другой порт
```bash
python manage.py runserver 8001
```

### Проблема: "Database is locked"
**Решение:** Закройте все процессы Django и перезапустите
```bash
# Windows
taskkill /f /im python.exe
# Затем перезапустите сервер
```

### Проблема: Статические файлы не загружаются
**Решение:** Соберите статические файлы
```bash
python manage.py collectstatic
```

### Проблема: Ошибки миграций
**Решение:** Сбросьте миграции
```bash
python manage.py migrate --fake-initial
```

## 📊 Проверка работоспособности

### 1. Проверка данных
```bash
python scripts/check_data.py
```

### 2. Проверка страниц
- Откройте http://127.0.0.1:8000/
- Проверьте все разделы меню
- Убедитесь, что контент отображается корректно

### 3. Проверка админки
- Откройте http://127.0.0.1:8000/admin/
- Войдите с учетными данными суперпользователя
- Проверьте доступ к моделям

## 🔄 Перезапуск проекта

### Полный перезапуск:
```bash
# 1. Остановить сервер (Ctrl+C)
# 2. Активировать окружение
.\venv\Scripts\activate

# 3. Проверить данные
python scripts/check_data.py

# 4. Запустить сервер
python manage.py runserver
```

## 📚 Дополнительная документация

- **[QUICK_CONTEXT.md](QUICK_CONTEXT.md)** - быстрый контекст проекта
- **[PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)** - полный контекст проекта
- **[DJANGO_PROJECT_PLAN.md](DJANGO_PROJECT_PLAN.md)** - план разработки
- **[DATA_CLEANUP_TASK.md](DATA_CLEANUP_TASK.md)** - решение проблем с данными

---

**Статус проекта:** Готов к работе  
**Последнее обновление:** 26 августа 2025


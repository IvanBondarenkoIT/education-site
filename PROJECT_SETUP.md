# Инструкции по настройке и запуску проекта "Дом Кофе"

## Активация виртуального окружения

### Windows PowerShell:
```powershell
# Активация виртуального окружения
.\venv\Scripts\Activate.ps1

# Или альтернативный способ:
venv\Scripts\Activate.ps1
```

### Windows Command Prompt:
```cmd
# Активация виртуального окружения
venv\Scripts\activate.bat
```

### Linux/Mac:
```bash
# Активация виртуального окружения
source venv/bin/activate
```

## Установка зависимостей

После активации виртуального окружения:
```bash
pip install -r requirements.txt
```

## Запуск проекта

### 1. Применение миграций:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Создание суперпользователя:
```bash
python manage.py createsuperuser
```

### 3. Импорт данных (если нужно):
```bash
python manage.py import_all_data
```

### 4. Запуск сервера разработки:
```bash
python manage.py runserver
```

## Структура проекта

```
education_site/
├── core/                          # Основное приложение Django
├── education_site/                # Настройки проекта
├── static/                        # Статические файлы (CSS, JS, изображения)
├── media/                         # Загружаемые файлы
├── templates/                     # HTML шаблоны
├── locale/                        # Файлы переводов
├── data/                          # Исходные данные и CSV файлы
│   ├── raw/                       # Исходные HTML файлы
│   ├── processed/                 # Обработанные данные
│   └── imports/                   # Файлы для импорта
├── docs/                          # Документация
├── scripts/                       # Скрипты для обработки данных
├── venv/                          # Виртуальное окружение
├── manage.py
├── requirements.txt
└── README.md
```

## Команды для работы с данными

```bash
# Импорт всех данных
python manage.py import_all_data

# Импорт отдельных типов данных
python manage.py import_business_values
python manage.py import_training_program
python manage.py import_job_instructions
python manage.py import_coffee_info

# Создание начальных данных
python manage.py create_initial_data
```

## Настройка Git

### .gitignore файл должен исключать:
- venv/
- __pycache__/
- *.pyc
- db.sqlite3
- media/
- staticfiles/
- .env
- *.log

## Полезные команды Django

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сбор статических файлов
python manage.py collectstatic

# Создание файлов переводов
python manage.py makemessages -l ru -l uk -l en -l ge

# Компиляция переводов
python manage.py compilemessages
```

## Отладка

### Проверка установленных пакетов:
```bash
pip list
```

### Проверка версии Python:
```bash
python --version
```

### Проверка версии Django:
```bash
python -c "import django; print(django.get_version())"
```

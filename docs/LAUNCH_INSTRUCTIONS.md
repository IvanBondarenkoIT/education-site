# 🚀 ИНСТРУКЦИИ ПО ЗАПУСКУ ПРОЕКТА "ДОМ КОФЕ"

## 📋 **БЫСТРЫЙ СТАРТ**

### **1. Локальный запуск (для разработки):**

```bash
# 1. Активация виртуального окружения
cd "D:\Education Site"
.\venv\Scripts\activate

# 2. Проверка данных
python scripts/check_data.py

# 3. Запуск сервера
python manage.py runserver
```

### **2. Проверка доступных URL:**

- **Главная страница:** http://127.0.0.1:8000/
- **Программа обучения:** http://127.0.0.1:8000/training/
- **Должностные инструкции:** http://127.0.0.1:8000/instructions/
- **Информация о кофе:** http://127.0.0.1:8000/coffee-info/
- **Бизнес-ценности:** http://127.0.0.1:8000/business-values/
- **Админка:** http://127.0.0.1:8000/admin/

## 🔧 **ПОЛНАЯ НАСТРОЙКА**

### **Требования:**
- Python 3.11+
- Git
- Виртуальное окружение

### **Установка зависимостей:**
```bash
# Активация окружения
.\venv\Scripts\activate

# Установка пакетов
pip install -r requirements.txt
```

### **Настройка базы данных:**
```bash
# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
```

### **Импорт данных:**
```bash
# Создание языков
python manage.py create_initial_data

# Импорт всех данных
python manage.py import_all_data

# Или по отдельности:
python manage.py import_business_values
python manage.py import_training_program
python manage.py import_job_instructions
python manage.py import_coffee_info
```

### **Сбор статических файлов:**
```bash
python manage.py collectstatic --noinput
```

## 🚀 **ДЕПЛОЙ НА RAILWAY**

### **Автоматический деплой:**
1. **Проект уже настроен** для автоматического деплоя
2. **Все файлы готовы:** `railway.json`, `Procfile`, `runtime.txt`
3. **Данные будут импортированы** автоматически при деплое

### **Проверка деплоя:**
1. Откройте Railway Dashboard
2. Проверьте логи деплоя
3. Убедитесь, что все команды выполнились успешно
4. Проверьте работу приложения по URL

## 📊 **ПРОВЕРКА ДАННЫХ**

### **Локальная проверка:**
```bash
python scripts/check_data.py
```

### **Ожидаемый результат:**
```
Статистика данных:
• BusinessValue: 33 записи
• TrainingProgram: 8 записей
• JobInstruction: 9 записей
• CoffeeInfo: 5 записей
• Language: 4 записи
```

### **Проверка через Django shell:**
```python
python manage.py shell

from core.models import *
print(f"Languages: {Language.objects.count()}")
print(f"Business Values: {BusinessValue.objects.count()}")
print(f"Training Programs: {TrainingProgram.objects.count()}")
print(f"Job Instructions: {JobInstruction.objects.count()}")
print(f"Coffee Info: {CoffeeInfo.objects.count()}")
```

## 🔍 **УСТРАНЕНИЕ ПРОБЛЕМ**

### **Проблема: "No module named 'django'"**
```bash
# Решение: активируйте виртуальное окружение
.\venv\Scripts\activate
```

### **Проблема: "Database table does not exist"**
```bash
# Решение: примените миграции
python manage.py migrate
```

### **Проблема: "Static files not found"**
```bash
# Решение: соберите статические файлы
python manage.py collectstatic --noinput
```

### **Проблема: "No data in models"**
```bash
# Решение: импортируйте данные
python manage.py import_all_data
```

## 📁 **СТРУКТУРА КОМАНД**

### **Основные команды:**
- `python manage.py runserver` - запуск сервера разработки
- `python manage.py migrate` - применение миграций
- `python manage.py collectstatic` - сбор статических файлов
- `python manage.py createsuperuser` - создание админа

### **Команды импорта данных:**
- `python manage.py create_initial_data` - создание языков
- `python manage.py import_business_values` - импорт бизнес-ценностей
- `python manage.py import_training_program` - импорт обучения
- `python manage.py import_job_instructions` - импорт инструкций
- `python manage.py import_coffee_info` - импорт информации о кофе
- `python manage.py import_all_data` - импорт всех данных

### **Команды проверки:**
- `python scripts/check_data.py` - проверка данных
- `python manage.py check` - проверка конфигурации
- `python manage.py showmigrations` - показ миграций

## 🎯 **ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ**

### **Основные страницы:**
- [ ] Главная страница загружается
- [ ] Навигация работает
- [ ] Многоязычность функционирует
- [ ] Статические файлы загружаются

### **Контент:**
- [ ] Бизнес-ценности отображаются (33 записи)
- [ ] Программа обучения работает (8 этапов)
- [ ] Должностные инструкции доступны (9 позиций)
- [ ] Информация о кофе загружается (5 статей)

### **Админка:**
- [ ] Доступ к админке: `/admin/`
- [ ] Все модели отображаются
- [ ] Данные можно редактировать
- [ ] Многоязычность работает

## 📞 **ПОДДЕРЖКА**

### **Документация:**
- **Контекст проекта:** `docs/PROJECT_CONTEXT.md`
- **Анализ данных:** `docs/DATA_ANALYSIS.md`
- **Чек-лист Railway:** `docs/RAILWAY_CHECKLIST.md`
- **План проекта:** `docs/DJANGO_PROJECT_PLAN.md`

### **Полезные команды:**
```bash
# Проверка статуса Git
git status

# Просмотр логов
python manage.py runserver --verbosity=2

# Очистка кэша
python manage.py clearcache
```

---

**Статус:** ✅ **Готов к использованию**
**Последнее обновление:** Декабрь 2024
**Версия:** 1.0.0


# 🏠 DIM KAVA - Образовательная платформа

**Образовательная платформа для сотрудников кофейной сети "Dim Kava"**

## 🎯 **О ПРОЕКТЕ**

Образовательная платформа предоставляет сотрудникам доступ к:
- 📚 **Программе обучения** - структурированные этапы обучения
- 👔 **Должностным инструкциям** - подробные инструкции для каждой позиции
- ☕ **Информации о кофе** - образовательный контент о кофе и зерне
- 💼 **Бизнес-ценностям** - корпоративные ценности и принципы

## 🌐 **МНОГОЯЗЫЧНОСТЬ**

Поддержка 4 языков:
- 🇷🇺 Русский (основной)
- 🇺🇦 Украинский
- 🇬🇧 Английский
- 🇬🇪 Грузинский

## 🚀 **БЫСТРЫЙ СТАРТ**

### **Локальный запуск:**
```bash
# 1. Активация окружения
cd "D:\Education Site"
.\venv\Scripts\activate

# 2. Проверка данных
python scripts/check_data.py

# 3. Запуск сервера
python manage.py runserver
```

### **Доступные URL:**
- **Главная:** http://127.0.0.1:8000/
- **Обучение:** http://127.0.0.1:8000/training/
- **Инструкции:** http://127.0.0.1:8000/instructions/
- **Кофе:** http://127.0.0.1:8000/coffee-info/
- **Ценности:** http://127.0.0.1:8000/business-values/
- **Админка:** http://127.0.0.1:8000/admin/

## 📊 **ДАННЫЕ ПРОЕКТА**

| Модель | Количество | Описание |
|--------|------------|----------|
| Language | 4 | Языки сайта |
| BusinessValue | 33 | Бизнес-ценности компании |
| TrainingProgram | 8 | Этапы программы обучения |
| JobInstruction | 9 | Должностные инструкции |
| CoffeeInfo | 5 | Статьи о кофе |
| **ИТОГО** | **59 записей** | **Все данные готовы** |

## 🏗️ **ТЕХНОЛОГИИ**

### **Backend:**
- **Django 5.2.5** - основной фреймворк
- **PostgreSQL** - база данных (Railway)
- **django-modeltranslation** - многоязычность
- **django-ckeditor** - rich text редактор
- **whitenoise** - статические файлы

### **Frontend:**
- **Django Templates** - шаблоны
- **CSS** - модульная структура стилей
- **Vanilla JavaScript** - интерактивность
- **Mobile-first** - адаптивный дизайн

## 🚀 **ДЕПЛОЙ НА RAILWAY**

### **Статус:** ✅ **Готов к деплою**

**Автоматические команды при деплое:**
```bash
python manage.py migrate
python manage.py create_initial_data
python manage.py import_business_values
python manage.py import_training_program
python manage.py import_job_instructions
python manage.py import_coffee_info
python manage.py collectstatic --noinput
gunicorn education_site.wsgi
```

### **Файлы конфигурации:**
- ✅ `railway.json` - настройки Railway
- ✅ `Procfile` - команда запуска
- ✅ `runtime.txt` - версия Python
- ✅ `requirements.txt` - зависимости

## 📁 **СТРУКТУРА ПРОЕКТА**

```
education-site/
├── core/                    # Основное приложение
│   ├── models.py           # Модели данных
│   ├── views.py            # Views
│   ├── urls.py             # URL маршруты
│   └── management/         # Команды импорта
├── education_site/         # Настройки проекта
├── templates/              # HTML шаблоны
├── static/                 # Статические файлы
├── data/                   # Данные для импорта
├── docs/                   # Документация
├── requirements.txt        # Зависимости
├── Procfile               # Railway конфигурация
├── runtime.txt            # Версия Python
└── railway.json           # Railway настройки
```

## 🔧 **КОМАНДЫ ИМПОРТА**

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

## 📚 **ДОКУМЕНТАЦИЯ**

- **[Контекст проекта](docs/PROJECT_CONTEXT.md)** - полное описание
- **[Анализ данных](docs/DATA_ANALYSIS.md)** - структура данных
- **[Инструкции запуска](docs/LAUNCH_INSTRUCTIONS.md)** - как запустить
- **[Чек-лист Railway](docs/RAILWAY_CHECKLIST.md)** - деплой на Railway

## 🎨 **ДИЗАЙН**

### **Цветовая схема:**
- Основной: #2C3E50 (темно-синий)
- Акцентный: #E67E22 (оранжевый)
- Фон: #ECF0F1 (светло-серый)

### **Компоненты:**
- Навигационное меню
- Языковой переключатель
- Карточки контента
- Адаптивная верстка

## 🔍 **ПРОВЕРКА РАБОТЫ**

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

## 🎯 **ЦЕЛИ ПРОЕКТА**

1. **Образование** - доступ к обучающим материалам
2. **Стандартизация** - единые стандарты работы
3. **Многоязычность** - поддержка 4 языков
4. **Доступность** - простой интерфейс
5. **Масштабируемость** - добавление контента

## 📞 **ПОДДЕРЖКА**

### **Полезные команды:**
```bash
# Проверка статуса
git status

# Проверка данных
python scripts/check_data.py

# Запуск сервера
python manage.py runserver
```

### **Устранение проблем:**
- **"No module named 'django'"** → активируйте виртуальное окружение
- **"Database table does not exist"** → выполните `python manage.py migrate`
- **"Static files not found"** → выполните `python manage.py collectstatic`

---

**Статус:** ✅ **Готов к деплою на Railway**
**Версия:** 1.0.0
**Последнее обновление:** Декабрь 2024

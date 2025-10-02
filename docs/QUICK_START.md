# 🚀 Быстрый запуск проекта "Dim Kava"

## ✅ Правильная последовательность команд

### 1. Активация виртуального окружения (Windows PowerShell)
```powershell
.\venv\Scripts\Activate.ps1
```

**Результат:** В начале строки должно появиться `(venv)`

### 2. Проверка окружения
```bash
python --version
pip list
```

### 3. Проверка проекта
```bash
python manage.py check
```

### 4. Применение миграций (если нужно)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Импорт данных (если нужно)
```bash
python manage.py import_all_data
```

### 6. Запуск сервера
```bash
python manage.py runserver
```

## 🌐 Доступ к сайту

После запуска сервера сайт будет доступен по адресам:
- **Главная страница:** http://127.0.0.1:8000/
- **Админка:** http://127.0.0.1:8000/admin/

## 📁 Структура после реорганизации

```
education_site/
├── core/                          # Django приложение
├── education_site/                # Настройки проекта
├── static/                        # CSS, JS, изображения
├── templates/                     # HTML шаблоны
├── data/                          # Данные проекта
│   ├── raw/                       # Исходные .txt файлы
│   ├── processed/                 # Обработанные .csv файлы
│   └── imports/                   # Скрипты импорта
├── docs/                          # Документация
├── scripts/                       # Дополнительные скрипты
├── venv/                          # Виртуальное окружение
├── manage.py                      # Управление Django
├── requirements.txt               # Зависимости
├── .gitignore                     # Исключения Git
└── README.md                      # Основная документация
```

## 🔧 Полезные команды

### Проверка статуса
```bash
python manage.py check
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Сбор статических файлов
```bash
python manage.py collectstatic
```

### Работа с переводами
```bash
python manage.py makemessages -l ru -l uk -l en -l ge
python manage.py compilemessages
```

## 🚨 Решение проблем

### Проблема: "No module named 'django'"
**Решение:** Виртуальное окружение не активировано
```powershell
.\venv\Scripts\Activate.ps1
```

### Проблема: "manage.py not found"
**Решение:** Файл был перемещен, верните его в корень проекта

### Проблема: Ошибки миграций
**Решение:** Пересоздайте миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📋 Чек-лист запуска

- [ ] Виртуальное окружение активировано `(venv)`
- [ ] Python 3.8+ установлен
- [ ] Django установлен (`pip list` показывает Django)
- [ ] `manage.py` находится в корне проекта
- [ ] `python manage.py check` проходит без ошибок
- [ ] Сервер запускается без ошибок
- [ ] Сайт доступен по http://127.0.0.1:8000/

## 🎯 Следующие шаги

1. **Импорт данных:** `python manage.py import_all_data`
2. **Создание админа:** `python manage.py createsuperuser`
3. **Настройка переводов:** Создание .po файлов
4. **Кастомизация дизайна:** Редактирование CSS/HTML
5. **Тестирование:** Проверка всех функций

---

**Последнее обновление:** 26 августа 2025


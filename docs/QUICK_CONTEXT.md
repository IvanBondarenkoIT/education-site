# ⚡ БЫСТРЫЙ КОНТЕКСТ ПРОЕКТА

## 🎯 Что это?
Django сайт "Дом Кофе" - образовательный портал для кофейной компании с многоязычностью.

## 📍 Где мы сейчас?
- **Этап:** 5 (Перенос контента из HTML)
- **Задача:** 5.13 Подготовить переводы для всех текстов
- **Выполнено:** 50/59 задач

## 🚀 Быстрый старт
```bash
cd "D:\Education Site"
.\venv\Scripts\activate
python manage.py runserver
```

## 📊 Данные в БД
- **BusinessValue:** 33 записи ✅
- **TrainingProgram:** 8 записей ✅
- **JobInstruction:** 9 записей ✅
- **CoffeeInfo:** 5 записей ✅

## 🌐 URL
- Главная: http://127.0.0.1:8000/
- Обучение: http://127.0.0.1:8000/training/
- Инструкции: http://127.0.0.1:8000/instructions/
- Кофе: http://127.0.0.1:8000/coffee-info/
- Ценности: http://127.0.0.1:8000/business-values/

## 🔧 Полезные команды
```bash
python scripts/check_data.py                    # Проверка данных
python manage.py clear_incorrect_data --confirm # Очистка данных
python manage.py import_training_program        # Импорт обучения
python manage.py import_job_instructions        # Импорт инструкций
python manage.py import_coffee_info             # Импорт кофе
```

## 🚨 Решенные проблемы
- ✅ HTML-мусор в данных (используем CSV из data/processed/)
- ✅ Дублирование данных (очистили и переимпортировали)

## 📚 Документация
- `docs/PROJECT_CONTEXT.md` - полный контекст
- `docs/DJANGO_PROJECT_PLAN.md` - план проекта
- `docs/DATA_CLEANUP_TASK.md` - решение проблем с данными

## 🎯 Следующий шаг
Задача 5.13: Подготовить переводы для всех текстов (ru, uk, en, ge)

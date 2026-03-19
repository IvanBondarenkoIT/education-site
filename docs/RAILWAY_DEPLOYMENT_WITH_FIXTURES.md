# 🚀 ДЕПЛОЙ НА RAILWAY С ФИКСТУРАМИ

## ✅ Что готово

- **Фикстуры созданы:** `core/fixtures/all_data.json` (59 записей)
- **Railway настроен:** `railway.json` обновлен для загрузки фикстур
- **Команды готовы:** `load_fixtures`, `export_fixtures`
- **Fallback работает:** импорт из файлов для локальной разработки

## 🔧 Команды Railway

### Старый вариант (не работал):
```bash
python manage.py import_business_values
python manage.py import_training_program
python manage.py import_job_instructions
python manage.py import_coffee_info
```

### Текущий вариант (идемпотентный, при каждом деплое):
```bash
python manage.py load_fixtures --clear
```
Очищает контент-модели и загружает свежие данные из `all_data.json`. Гарантирует актуальность контента при повторных деплоях.

## 📊 Ожидаемый результат

После деплоя на Railway:
- ✅ БД автоматически заполняется данными
- ✅ Все 59 записей доступны
- ✅ Сайт работает с полным контентом

## 🚀 Быстрый деплой

1. **Закоммитить изменения:**
   ```bash
   git add .
   git commit -m "feat: Замена импорта на фикстуры для Railway"
   git push origin main
   ```

2. **Railway автоматически:**
   - Применит миграции
   - Загрузит фикстуры (`load_fixtures --clear`)
   - Создаст админа (`create_default_admin`)
   - Соберет статические файлы
   - Запустит приложение

   **Важно:** Задайте `ADMIN_PASSWORD` в переменных окружения Railway для продакшена.

3. **Проверить результат:**
   - Открыть Railway Dashboard
   - Проверить логи деплоя
   - Убедиться в отсутствии ошибок "Файл не найден"

## 🔍 Проверка данных

После деплоя проверить:
- Language: 4 записи
- BusinessValue: 33 записи
- TrainingProgram: 8 записей
- JobInstruction: 9 записей
- CoffeeInfo: 5 записей

**ИТОГО: 59 записей**

## 📝 Обновление контента (content/ → Railway)

1. Редактировать файлы в `content/` (markdown).
2. Локально: `python manage.py sync_content_from_md --clear` — синхронизирует в БД и обновляет `all_data.json`.
3. Коммит и push: `git add core/fixtures/all_data.json && git commit -m "Update content" && git push`.
4. Railway при деплое выполнит `load_fixtures --clear` и подхватит новый контент.

## 📁 Структура фикстур

```
core/fixtures/
└── all_data.json          # Все данные (400KB, 59 записей)
```

## 🎯 Критерии успеха

- [ ] Деплой проходит без ошибок
- [ ] БД заполняется автоматически
- [ ] Все страницы загружаются
- [ ] Данные отображаются корректно

---

**Статус:** ✅ Готов к деплою  
**Время настройки:** 40 минут  
**Сложность:** Средняя

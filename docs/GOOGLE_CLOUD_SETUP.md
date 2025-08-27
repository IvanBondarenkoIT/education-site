# ☁️ НАСТРОЙКА GOOGLE CLOUD PLATFORM ДЛЯ ДЕПЛОЯ

## 📋 Предварительные требования

### 1. Google Аккаунт
- У вас должен быть Google аккаунт (Gmail)
- Рекомендуется использовать аккаунт, который не связан с критически важными сервисами

### 2. Кредитная карта
- **Обязательно** для активации бесплатного уровня
- Google не будет списывать деньги без вашего согласия
- Можно установить лимиты расходов

## 🚀 Пошаговая настройка Google Cloud

### Шаг 1: Регистрация в Google Cloud Platform

1. **Перейдите на сайт Google Cloud:**
   ```
   https://cloud.google.com/
   ```

2. **Нажмите "Get started for free" или "Начать бесплатно"**

3. **Войдите в свой Google аккаунт**

4. **Заполните форму регистрации:**
   - **Страна:** Россия
   - **Имя:** Ваше имя
   - **Email:** Ваш Gmail
   - **Согласие с условиями:** Поставьте галочки

### Шаг 2: Активация бесплатного уровня

1. **Введите данные кредитной карты:**
   - Номер карты
   - Срок действия
   - CVV код
   - Имя владельца
   - Адрес

2. **Важно:** Google не спишет деньги автоматически!
   - Списывается только $1 для проверки карты (возвращается)
   - Все остальное бесплатно в рамках лимитов

3. **Нажмите "Start my free trial"**

### Шаг 3: Создание проекта

1. **После активации создайте новый проект:**
   - Нажмите "Select a project" в верхней панели
   - Нажмите "New Project"

2. **Заполните данные проекта:**
   - **Project name:** `dom-kofe-education`
   - **Project ID:** `dom-kofe-education-XXXXX` (автоматически)
   - **Location:** Оставьте пустым

3. **Нажмите "Create"**

### Шаг 4: Включение необходимых API

1. **Перейдите в "APIs & Services" > "Library"**

2. **Включите следующие API (нажмите "Enable" для каждого):**

   #### Обязательные API:
   - **Cloud Build API** - для сборки приложения
   - **Cloud Run API** - для запуска приложения
   - **Cloud SQL Admin API** - для базы данных
   - **Secret Manager API** - для хранения секретов

   #### Дополнительные API:
   - **Cloud Storage API** - для статических файлов
   - **Cloud Logging API** - для логов
   - **Cloud Monitoring API** - для мониторинга

### Шаг 5: Настройка сервисного аккаунта

1. **Перейдите в "IAM & Admin" > "Service Accounts"**

2. **Нажмите "Create Service Account"**

3. **Заполните данные:**
   - **Service account name:** `django-app-service`
   - **Service account ID:** `django-app-service`
   - **Description:** `Service account for Django application`

4. **Нажмите "Create and Continue"**

5. **Назначьте роли (нажмите "Select a role" для каждой):**
   - **Cloud Run Admin** - для управления приложением
   - **Cloud SQL Admin** - для управления базой данных
   - **Secret Manager Secret Accessor** - для доступа к секретам
   - **Storage Object Admin** - для статических файлов

6. **Нажмите "Continue" и "Done"**

### Шаг 6: Создание ключа сервисного аккаунта

1. **В списке сервисных аккаунтов найдите созданный**

2. **Нажмите на email аккаунта**

3. **Перейдите на вкладку "Keys"**

4. **Нажмите "Add Key" > "Create new key"**

5. **Выберите "JSON" и нажмите "Create"**

6. **Скачайте файл ключа** (сохраните в безопасном месте)

### Шаг 7: Настройка базы данных (Cloud SQL)

1. **Перейдите в "SQL" в боковом меню**

2. **Нажмите "Create Instance"**

3. **Выберите "PostgreSQL"**

4. **Заполните данные:**
   - **Instance ID:** `dom-kofe-db`
   - **Password:** Создайте надежный пароль (запишите!)
   - **Database version:** PostgreSQL 15
   - **Region:** `europe-west1` (Бельгия)

5. **Нажмите "Create Instance"**

### Шаг 8: Настройка Cloud Storage

1. **Перейдите в "Cloud Storage" > "Buckets"**

2. **Нажмите "Create Bucket"**

3. **Заполните данные:**
   - **Name:** `dom-kofe-static-files`
   - **Location type:** Region
   - **Location:** `europe-west1`
   - **Storage class:** Standard
   - **Access control:** Uniform

4. **Нажмите "Create"**

### Шаг 9: Настройка лимитов расходов

1. **Перейдите в "Billing" в боковом меню**

2. **Нажмите на ваш аккаунт биллинга**

3. **Перейдите в "Budgets & alerts"**

4. **Нажмите "Create Budget"**

5. **Настройте бюджет:**
   - **Budget name:** `Monthly Budget`
   - **Budget amount:** $5
   - **Budget period:** Monthly
   - **Alerts:** 50%, 80%, 100%

6. **Нажмите "Save"**

## 🔧 Установка Google Cloud CLI

### Windows (PowerShell):
```powershell
# Скачайте и установите Google Cloud CLI
# https://cloud.google.com/sdk/docs/install

# После установки откройте PowerShell и выполните:
gcloud init
```

### Проверка установки:
```bash
gcloud --version
gcloud auth list
```

## 📊 Бесплатные лимиты Google Cloud

### App Engine:
- **28 часов в день** бесплатно
- **1GB RAM** на инстанс
- **Автоматическое масштабирование**

### Cloud SQL:
- **1GB** PostgreSQL бесплатно
- **1 инстанс** в бесплатном плане

### Cloud Storage:
- **5GB** бесплатно
- **1GB исходящего трафика** в день

### Cloud Build:
- **120 минут в день** бесплатно

## 🚨 Важные предупреждения

### Безопасность:
- ✅ **Не публикуйте** ключ сервисного аккаунта
- ✅ **Установите лимиты расходов**
- ✅ **Регулярно проверяйте** использование ресурсов

### Мониторинг:
- 📊 **Проверяйте** панель биллинга еженедельно
- 🔔 **Настройте уведомления** о расходах
- 📈 **Следите за** использованием ресурсов

## 🎯 Следующие шаги

После настройки Google Cloud:

1. **Установите Google Cloud CLI**
2. **Настройте проект локально**
3. **Подготовим Django проект к деплою**
4. **Выполним деплой на App Engine**

## 📞 Поддержка

### Полезные ссылки:
- [Google Cloud Console](https://console.cloud.google.com/)
- [Документация App Engine](https://cloud.google.com/appengine/docs)
- [Бесплатный уровень](https://cloud.google.com/free)

### В случае проблем:
- 📧 **Google Cloud Support** (если есть платная поддержка)
- 💬 **Stack Overflow** с тегом `google-cloud-platform`
- 📚 **Официальная документация**

---

**Статус:** Готов к настройке  
**Сложность:** Средняя  
**Время настройки:** 30-60 минут  
**Стоимость:** $0 (в рамках бесплатного уровня)

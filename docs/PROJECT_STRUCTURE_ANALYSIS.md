# Анализ структуры проекта "Дом Кофе"

## Общая информация
- **Проект**: Django-сайт для образовательного портала компании "Дом Кофе"
- **Назначение**: Внутренний образовательный портал для обучения сотрудников
- **Проблема**: Все модели в админке содержат одинаковый текстовый контент

## Структура проекта

### Основные директории
```
/
├── core/                    # Основное Django приложение
├── source/                  # Исходные HTML файлы с контентом
├── templates/               # Django шаблоны
├── static/                  # Статические файлы
├── media/                   # Загружаемые файлы
├── requirements.txt         # Зависимости Python
├── manage.py               # Django management
├── DJANGO_PROJECT_PLAN.md  # План проекта
├── IMPORT_COMMANDS.md      # Команды импорта данных
└── PROJECT_STRUCTURE_ANALYSIS.md # Этот файл
```

### Модели данных (core/models.py)

#### 1. **Course** - Курсы обучения
- `title` - Название курса
- `description` - Описание курса
- `duration` - Продолжительность
- `difficulty` - Сложность (choices)
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 2. **Module** - Модули курсов
- `course` - Связь с курсом (ForeignKey)
- `title` - Название модуля
- `description` - Описание модуля
- `order` - Порядок модуля
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 3. **Lesson** - Уроки
- `module` - Связь с модулем (ForeignKey)
- `title` - Название урока
- `content` - Содержание урока
- `order` - Порядок урока
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 4. **JobInstruction** - Должностные инструкции
- `title` - Название инструкции
- `position` - Должность (choices: MANAGER, BARISTA, etc.)
- `content` - Содержание инструкции
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 5. **CoffeeInfo** - Информация о кофе
- `title` - Название
- `category` - Категория (choices: BEANS, BREWING, etc.)
- `content` - Содержание
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 6. **BusinessValue** - Бизнес-ценности
- `title` - Название ценности
- `description` - Описание
- `content` - Содержание
- `created_at` - Дата создания
- `updated_at` - Дата обновления

#### 7. **Regulation** - Регламенты
- `title` - Название регламента
- `category` - Категория (choices: INVENTORY, SAFETY, etc.)
- `content` - Содержание регламента
- `created_at` - Дата создания
- `updated_at` - Дата обновления

### Исходные данные (source/)

#### Структура HTML файлов:
- **Главная страница.html** - Общая информация о портале
- **Добро пожаловать в команду Дом Кофе.html** - Приветствие новых сотрудников
- **Программа обучения новых сотрудников.html** - Общая программа обучения
- **Должностные инструкции/** - Папка с инструкциями по должностям
- **Информация о зерне/** - Папка с информацией о кофе
- **Регламенты/** - Папка с регламентами

#### Ключевые файлы:
- `Должностная инструкция менеджера магазина.html`
- `Информация о зерне.html`
- `Регламенты.html`
- `Главная страница.html`

### Django Views (core/views.py)

#### Основные представления:
1. **HomeView** - Главная страница
2. **CourseListView** - Список курсов
3. **CourseDetailView** - Детали курса
4. **JobInstructionListView** - Список должностных инструкций
5. **JobInstructionDetailView** - Детали инструкции
6. **CoffeeInfoListView** - Список информации о кофе
7. **CoffeeInfoDetailView** - Детали информации о кофе
8. **BusinessValuesView** - Бизнес-ценности
9. **RegulationListView** - Список регламентов
10. **RegulationDetailView** - Детали регламента

### URL маршруты (core/urls.py)

#### Основные URL:
- `/` - Главная страница
- `/courses/` - Список курсов
- `/courses/<int:pk>/` - Детали курса
- `/instructions/` - Должностные инструкции
- `/instructions/<int:pk>/` - Детали инструкции
- `/coffee-info/` - Информация о кофе
- `/coffee-info/<int:pk>/` - Детали информации о кофе
- `/business-values/` - Бизнес-ценности
- `/regulations/` - Регламенты
- `/regulations/<int:pk>/` - Детали регламента

### Шаблоны (templates/)

#### Основные шаблоны:
- `base.html` - Базовый шаблон
- `home.html` - Главная страница
- `courses/course_list.html` - Список курсов
- `courses/course_detail.html` - Детали курса
- `instructions/job_instruction_list.html` - Список инструкций
- `instructions/job_instruction_detail.html` - Детали инструкции
- `coffee_info/coffee_info_list.html` - Список информации о кофе
- `coffee_info/coffee_info_detail.html` - Детали информации о кофе
- `business_values.html` - Бизнес-ценности
- `regulations/regulation_list.html` - Список регламентов
- `regulations/regulation_detail.html` - Детали регламента

## Текущая проблема

**Все модели в админке содержат одинаковый текстовый контент** - это означает, что данные не были правильно импортированы из исходных HTML файлов в папке `source/`.

## Задача

1. **Проанализировать** содержимое HTML файлов в папке `source/`
2. **Структурировать** данные согласно моделям Django
3. **Создать** CSV файлы с правильными данными для каждой модели
4. **Подготовить** команды импорта данных в Django

## Категории данных

### Должностные инструкции (JobInstruction)
- **Должности**: MANAGER, BARISTA, CASHIER, SUPERVISOR, ADMINISTRATOR
- **Файлы**: Все файлы в папке "Должностные инструкции"

### Информация о кофе (CoffeeInfo)
- **Категории**: BEANS, BREWING, GRADING, EXTRACTION, DECAFFEINATED, MARKING, WORLD_CLASSICS
- **Файлы**: Все файлы в папке "Информация о зерне"

### Регламенты (Regulation)
- **Категории**: INVENTORY, SAFETY, QUALITY, OPERATIONS, CUSTOMER_SERVICE
- **Файлы**: Все файлы в папке "Регламенты"

### Бизнес-ценности (BusinessValue)
- **Файлы**: Содержимое из файлов с бизнес-ценностями

### Курсы (Course/Module/Lesson)
- **Файлы**: Структурированные данные из программы обучения


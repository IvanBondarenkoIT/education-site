# Generated manually for initial models

from django.db import migrations, models
import django.db.models.deletion
import ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.TextField(help_text='Описание ситуации', verbose_name='Ситуация')),
                ('business_value', models.TextField(help_text='Объяснение бизнес-ценности', verbose_name='Бизнес ценность')),
                ('category', models.CharField(choices=[('competence', 'Компетентность'), ('leadership', 'Лидерство'), ('uniqueness', 'Уникальность'), ('team', 'Команда'), ('espresso_culture', 'Эспрессо культура')], max_length=20, verbose_name='Категория')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Бизнес ценность',
                'verbose_name_plural': 'Бизнес ценности',
                'ordering': ['category', 'order'],
            },
        ),
        migrations.CreateModel(
            name='CoffeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('beans', 'Зерно'), ('roasting', 'Обжарка'), ('brewing', 'Приготовление'), ('varieties', 'Сорта'), ('history', 'История'), ('culture', 'Культура')], max_length=20, verbose_name='Категория')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='coffee_info/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Информация о кофе',
                'verbose_name_plural': 'Информация о кофе',
                'ordering': ['category', 'order'],
            },
        ),
        migrations.CreateModel(
            name='JobInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('manager', 'Менеджер магазина'), ('senior_barista', 'Старший бариста'), ('barista', 'Бариста'), ('cashier', 'Кассир'), ('cook', 'Повар'), ('cleaner', 'Уборщик'), ('delivery_driver', 'Водитель доставки')], max_length=50, verbose_name='Должность')),
                ('department', models.CharField(choices=[('management', 'Менеджмент'), ('barista', 'Бариста'), ('cashier', 'Кассир'), ('kitchen', 'Кухня'), ('cleaning', 'Уборка'), ('delivery', 'Доставка')], max_length=20, verbose_name='Отдел')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержание инструкции')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Должностная инструкция',
                'verbose_name_plural': 'Должностные инструкции',
                'ordering': ['department', 'position', 'order'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='ru, uk, en, ge', max_length=5, unique=True, verbose_name='Код языка')),
                ('name', models.CharField(help_text='Русский, Українська, English, ქართული', max_length=50, verbose_name='Название')),
                ('flag_icon', models.CharField(help_text='🇷🇺, 🇺🇦, 🇬🇧, 🇬🇪', max_length=20, verbose_name='Иконка флага')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_default', models.BooleanField(default=False, verbose_name='По умолчанию')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('period_type', models.CharField(choices=[('day', 'День'), ('week', 'Неделя'), ('month', 'Месяц')], max_length=10, verbose_name='Тип периода')),
                ('period_number', models.PositiveIntegerField(help_text='День 1, Неделя 2, Месяц 3 и т.д.', verbose_name='Номер периода')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Программа обучения',
                'verbose_name_plural': 'Программы обучения',
                'ordering': ['period_type', 'period_number', 'order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='trainingprogram',
            unique_together={('period_type', 'period_number')},
        ),
    ]


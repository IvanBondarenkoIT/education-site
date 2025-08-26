
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from ckeditor.fields import RichTextField
from modeltranslation.translator import translator, TranslationOptions, register

# Create your models here.

class Page(models.Model):
    """Базовая модель для всех страниц сайта"""
    title = models.CharField(_('Заголовок'), max_length=200)
    slug = models.SlugField(_('URL'), max_length=200, unique=True)
    content = RichTextField(_('Содержание'), blank=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    is_active = models.BooleanField(_('Активна'), default=True)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    
    class Meta:
        verbose_name = _('Страница')
        verbose_name_plural = _('Страницы')
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})


class BusinessValue(models.Model):
    """Модель для бизнес-ценностей компании (33 пункта)"""
    CATEGORY_CHOICES = [
        ('competence', _('Компетентность')),
        ('leadership', _('Лидерство')),
        ('uniqueness', _('Уникальность')),
        ('team', _('Команда')),
        ('espresso_culture', _('Эспрессо культура')),
    ]
    
    situation = models.TextField(_('Ситуация'), help_text=_('Описание ситуации'))
    business_value = models.TextField(_('Бизнес ценность'), help_text=_('Объяснение бизнес-ценности'))
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    
    class Meta:
        verbose_name = _('Бизнес ценность')
        verbose_name_plural = _('Бизнес ценности')
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.situation[:50]}..."


class TrainingProgram(models.Model):
    """Модель для программы обучения сотрудников"""
    PERIOD_CHOICES = [
        ('day', _('День')),
        ('week', _('Неделя')),
        ('month', _('Месяц')),
    ]
    
    title = models.CharField(_('Заголовок'), max_length=200)
    content = RichTextField(_('Содержание'))
    period_type = models.CharField(_('Тип периода'), max_length=10, choices=PERIOD_CHOICES)
    period_number = models.PositiveIntegerField(_('Номер периода'), help_text=_('День 1, Неделя 2, Месяц 3 и т.д.'))
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    
    class Meta:
        verbose_name = _('Программа обучения')
        verbose_name_plural = _('Программы обучения')
        ordering = ['period_type', 'period_number', 'order']
        unique_together = ['period_type', 'period_number']
    
    def __str__(self):
        return f"{self.get_period_type_display()} {self.period_number}: {self.title}"
    
    def get_period_display(self):
        return f"{self.get_period_type_display()} {self.period_number}"


class JobInstruction(models.Model):
    """Модель для должностных инструкций"""
    DEPARTMENT_CHOICES = [
        ('management', _('Менеджмент')),
        ('barista', _('Бариста')),
        ('cashier', _('Кассир')),
        ('kitchen', _('Кухня')),
        ('cleaning', _('Уборка')),
        ('delivery', _('Доставка')),
    ]
    
    POSITION_CHOICES = [
        ('manager', _('Менеджер магазина')),
        ('senior_barista', _('Старший бариста')),
        ('barista', _('Бариста')),
        ('cashier', _('Кассир')),
        ('cook', _('Повар')),
        ('cleaner', _('Уборщик')),
        ('delivery_driver', _('Водитель доставки')),
    ]
    
    position = models.CharField(_('Должность'), max_length=50, choices=POSITION_CHOICES)
    department = models.CharField(_('Отдел'), max_length=20, choices=DEPARTMENT_CHOICES)
    title = models.CharField(_('Заголовок'), max_length=200)
    content = RichTextField(_('Содержание инструкции'))
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    
    class Meta:
        verbose_name = _('Должностная инструкция')
        verbose_name_plural = _('Должностные инструкции')
        ordering = ['department', 'position', 'order']
    
    def __str__(self):
        return f"{self.get_position_display()}: {self.title}"


class CoffeeInfo(models.Model):
    """Модель для информации о кофе и зерне"""
    CATEGORY_CHOICES = [
        ('beans', _('Зерно')),
        ('roasting', _('Обжарка')),
        ('brewing', _('Приготовление')),
        ('varieties', _('Сорта')),
        ('history', _('История')),
        ('culture', _('Культура')),
    ]
    
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(_('Заголовок'), max_length=200)
    content = RichTextField(_('Содержание'))
    image = models.ImageField(_('Изображение'), upload_to='coffee_info/', blank=True, null=True)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    
    class Meta:
        verbose_name = _('Информация о кофе')
        verbose_name_plural = _('Информация о кофе')
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"


class Language(models.Model):
    """Модель для управления языками сайта"""
    code = models.CharField(_('Код языка'), max_length=5, unique=True, help_text=_('ru, uk, en, ge'))
    name = models.CharField(_('Название'), max_length=50, help_text=_('Русский, Українська, English, ქართული'))
    flag_icon = models.CharField(_('Иконка флага'), max_length=20, help_text=_('🇷🇺, 🇺🇦, 🇬🇧, 🇬🇪'))
    is_active = models.BooleanField(_('Активен'), default=True)
    is_default = models.BooleanField(_('По умолчанию'), default=False)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    
    class Meta:
        verbose_name = _('Язык')
        verbose_name_plural = _('Языки')
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.flag_icon} {self.name} ({self.code})"
    
    def save(self, *args, **kwargs):
        # Если этот язык становится языком по умолчанию, сбрасываем другие
        if self.is_default:
            Language.objects.filter(is_default=True).update(is_default=False)
        super().save(*args, **kwargs)


# Настройка переводов для моделей
class PageTranslation(TranslationOptions):
    fields = ('title', 'content')

class BusinessValueTranslation(TranslationOptions):
    fields = ('situation', 'business_value')

class TrainingProgramTranslation(TranslationOptions):
    fields = ('title', 'content')

class JobInstructionTranslation(TranslationOptions):
    fields = ('title', 'content')

class CoffeeInfoTranslation(TranslationOptions):
    fields = ('title', 'content')



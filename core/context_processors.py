from django.conf import settings
from django.utils.translation import get_language
from .models import Language


def language_info(request):
    """
    Контекстный процессор для добавления информации о языке
    """
    current_language = get_language()
    
    # Получаем информацию о текущем языке
    try:
        current_lang_obj = Language.objects.get(code=current_language)
    except Language.DoesNotExist:
        current_lang_obj = None
    
    # Получаем все активные языки
    active_languages = Language.objects.filter(is_active=True).order_by('order')
    
    # Получаем информацию о доступных языках
    available_languages = []
    for lang in active_languages:
        available_languages.append({
            'code': lang.code,
            'name': lang.name,
            'flag_icon': lang.flag_icon,
            'is_current': lang.code == current_language,
            'is_default': lang.is_default,
        })
    
    return {
        'current_language': current_language,
        'current_language_obj': current_lang_obj,
        'available_languages': available_languages,
        'languages': available_languages,  # Для совместимости
    }


def site_settings(request):
    """
    Контекстный процессор для общих настроек сайта
    """
    return {
        'site_name': 'Дом Кофе',
        'site_description': 'Образовательный портал для сотрудников кофейной компании',
        'site_keywords': 'кофе, обучение, бариста, менеджер, должностные инструкции, бизнес-ценности',
    }

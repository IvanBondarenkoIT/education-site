from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils.translation import get_language
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.urls import reverse
from .models import (
    Page, BusinessValue, TrainingProgram, 
    JobInstruction, CoffeeInfo, Language
)


def home(request):
    """
    Главная страница сайта
    """
    # Получаем статистику для отображения на главной
    stats = {
        'business_values_count': BusinessValue.objects.count(),
        'job_instructions_count': JobInstruction.objects.count(),
        'coffee_info_count': CoffeeInfo.objects.count(),
        'languages_count': Language.objects.filter(is_active=True).count(),
    }
    
    context = {
        'page_title': 'Dim Kava - Образовательный портал',
        'stats': stats,
    }
    
    return render(request, 'home.html', context)


def business_values(request):
    """
    Страница с бизнес-ценностями (таблица из 33 пунктов)
    """
    # Получаем все бизнес-ценности, сгруппированные по категориям
    business_values = BusinessValue.objects.all().order_by('category', 'order')
    
    # Группируем по категориям для удобного отображения
    categories = {}
    for value in business_values:
        if value.category not in categories:
            categories[value.category] = []
        categories[value.category].append(value)
    
    context = {
        'page_title': 'Бизнес-ценности компании',
        'business_values': business_values,
        'categories': categories,
        'total_count': business_values.count(),
    }
    
    return render(request, 'business_values.html', context)


def training_program(request):
    """
    Страница с программой обучения (по дням/неделям/месяцам)
    """
    # Получаем программы обучения, сгруппированные по периодам
    daily_programs = TrainingProgram.objects.filter(period_type='day').order_by('order')
    weekly_programs = TrainingProgram.objects.filter(period_type='week').order_by('order')
    monthly_programs = TrainingProgram.objects.filter(period_type='month').order_by('order')
    
    context = {
        'page_title': 'Программа обучения новых сотрудников',
        'daily_programs': daily_programs,
        'weekly_programs': weekly_programs,
        'monthly_programs': monthly_programs,
        'total_daily': daily_programs.count(),
        'total_weekly': weekly_programs.count(),
        'total_monthly': monthly_programs.count(),
    }
    
    return render(request, 'training/training_program.html', context)


def training_detail(request, program_id):
    """
    Детальная страница программы обучения
    """
    program = get_object_or_404(TrainingProgram, id=program_id)
    
    context = {
        'page_title': program.title,
        'program': program,
    }
    
    return render(request, 'training/training_detail.html', context)


def job_instructions(request):
    """
    Страница с должностными инструкциями
    """
    # Получаем инструкции, сгруппированные по отделам
    instructions = JobInstruction.objects.all().order_by('department', 'order')
    
    # Группируем по отделам
    departments = {}
    for instruction in instructions:
        if instruction.department not in departments:
            departments[instruction.department] = []
        departments[instruction.department].append(instruction)
    
    context = {
        'page_title': 'Должностные инструкции',
        'instructions': instructions,
        'departments': departments,
        'total_count': instructions.count(),
    }
    
    return render(request, 'instructions/job_instructions.html', context)


def job_instruction_detail(request, instruction_id):
    """
    Детальная страница должностной инструкции
    """
    instruction = get_object_or_404(JobInstruction, id=instruction_id)
    
    context = {
        'page_title': instruction.title,
        'instruction': instruction,
    }
    
    return render(request, 'instructions/job_instruction_detail.html', context)


def coffee_info(request):
    """
    Страница с информацией о кофе
    """
    # Получаем информацию о кофе, сгруппированную по категориям
    coffee_info_list = CoffeeInfo.objects.all().order_by('category', 'order')
    
    # Группируем по категориям
    categories = {}
    for info in coffee_info_list:
        if info.category not in categories:
            categories[info.category] = []
        categories[info.category].append(info)
    
    context = {
        'page_title': 'Информация о кофе и зерне',
        'coffee_info_list': coffee_info_list,
        'categories': categories,
        'total_count': coffee_info_list.count(),
    }
    
    return render(request, 'coffee_info/coffee_info.html', context)


def coffee_info_detail(request, info_id):
    """
    Детальная страница информации о кофе
    """
    coffee_info = get_object_or_404(CoffeeInfo, id=info_id)
    
    context = {
        'page_title': coffee_info.title,
        'coffee_info': coffee_info,
    }
    
    return render(request, 'coffee_info/coffee_info_detail.html', context)


def set_language(request):
    """
    View для переключения языка
    """
    from django.utils import translation
    from django.conf import settings
    
    if request.method == 'POST':
        language = request.POST.get('language')
        if language and language in [lang[0] for lang in settings.LANGUAGES]:
            translation.activate(language)
            request.session['django_language'] = language
            messages.success(request, f'Язык изменен на {dict(settings.LANGUAGES)[language]}')
    
    # Возвращаемся на предыдущую страницу или на главную
    return redirect(request.META.get('HTTP_REFERER', reverse('core:home')))


def page_not_found(request, exception):
    """
    404 страница
    """
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    """
    500 страница
    """
    return render(request, 'errors/500.html', status=500)


def permission_denied(request, exception):
    """
    403 страница
    """
    return render(request, 'errors/403.html', status=403)


def bad_request(request, exception):
    """
    400 страница
    """
    return render(request, 'errors/400.html', status=400)

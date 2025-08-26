from django.urls import path
from . import views

app_name = 'core'

# URL patterns для приложения core
urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    
    # Бизнес-ценности
    path('business-values/', views.business_values, name='business_values'),
    
    # Программа обучения
    path('training/', views.training_program, name='training_program'),
    path('training/<int:program_id>/', views.training_detail, name='training_detail'),
    
    # Должностные инструкции
    path('instructions/', views.job_instructions, name='job_instructions'),
    path('instructions/<int:instruction_id>/', views.job_instruction_detail, name='job_instruction_detail'),
    
    # Информация о кофе
    path('coffee-info/', views.coffee_info, name='coffee_info'),
    path('coffee-info/<int:info_id>/', views.coffee_info_detail, name='coffee_info_detail'),
    
    # Переключение языка
    path('set-language/', views.set_language, name='set_language'),
]

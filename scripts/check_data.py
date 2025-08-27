#!/usr/bin/env python
"""
Скрипт для проверки данных в моделях Django
"""

import os
import sys
import django

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_site.settings')
django.setup()

from core.models import BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo

def check_data():
    """Проверяет данные в моделях"""
    
    print("=" * 60)
    print("ПРОВЕРКА ДАННЫХ В МОДЕЛЯХ")
    print("=" * 60)
    
    # BusinessValue
    print(f"\n📊 BusinessValue: {BusinessValue.objects.count()} записей")
    if BusinessValue.objects.exists():
        print("Примеры записей:")
        for i, value in enumerate(BusinessValue.objects.all()[:3]):
            print(f"  {i+1}. {value.situation[:100]}...")
            print(f"     Категория: {value.get_category_display()}")
    
    # TrainingProgram
    print(f"\n📚 TrainingProgram: {TrainingProgram.objects.count()} записей")
    if TrainingProgram.objects.exists():
        print("Примеры записей:")
        for i, program in enumerate(TrainingProgram.objects.all()[:3]):
            print(f"  {i+1}. {program.title}")
            print(f"     Тип: {program.get_period_type_display()} {program.period_number}")
    
    # JobInstruction
    print(f"\n👔 JobInstruction: {JobInstruction.objects.count()} записей")
    if JobInstruction.objects.exists():
        print("Примеры записей:")
        for i, instruction in enumerate(JobInstruction.objects.all()[:3]):
            print(f"  {i+1}. {instruction.title}")
            print(f"     Должность: {instruction.get_position_display()}")
    
    # CoffeeInfo
    print(f"\n☕ CoffeeInfo: {CoffeeInfo.objects.count()} записей")
    if CoffeeInfo.objects.exists():
        print("Примеры записей:")
        for i, info in enumerate(CoffeeInfo.objects.all()[:3]):
            print(f"  {i+1}. {info.title}")
            print(f"     Категория: {info.get_category_display()}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    check_data()

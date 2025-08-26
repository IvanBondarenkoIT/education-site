from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import BusinessValue
from bs4 import BeautifulSoup
import os
import re


class Command(BaseCommand):
    help = 'Импортирует бизнес-ценности из HTML файла saved_resource.html'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='source/Добро пожаловать в команду Дом Кофе_files/saved_resource.html',
            help='Путь к HTML файлу с бизнес-ценностями'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед импортом'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Файл не найден: {file_path}')
            )
            return

        if options['clear']:
            BusinessValue.objects.all().delete()
            self.stdout.write('Существующие бизнес-ценности удалены')

        # Читаем HTML файл
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Парсим HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Находим таблицу
        table = soup.find('table')
        if not table:
            self.stdout.write(
                self.style.ERROR('Таблица не найдена в HTML файле')
            )
            return

        # Извлекаем данные из таблицы
        rows = table.find_all('tr')[1:]  # Пропускаем заголовок
        
        business_values_data = []
        
        for i, row in enumerate(rows, 1):
            cells = row.find_all('td')
            if len(cells) >= 2:
                situation_cell = cells[0]
                value_cell = cells[1]
                
                # Извлекаем текст ситуации
                situation_text = situation_cell.get_text(strip=True)
                # Убираем номер из начала
                situation_text = re.sub(r'^\d+\.\s*', '', situation_text)
                
                # Извлекаем бизнес-ценность
                business_value_text = value_cell.get_text(strip=True)
                # Убираем скобки
                business_value_text = re.sub(r'^\(|\)$', '', business_value_text)
                
                # Определяем категорию
                category = self.determine_category(business_value_text)
                
                business_values_data.append({
                    'situation': situation_text,
                    'business_value': business_value_text,
                    'category': category,
                    'order': i
                })

        # Создаем записи в базе данных
        created_count = 0
        for data in business_values_data:
            business_value, created = BusinessValue.objects.get_or_create(
                situation=data['situation'],
                defaults={
                    'business_value': data['business_value'],
                    'category': data['category'],
                    'order': data['order'],
                    'is_active': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    f'Создана бизнес-ценность: {data["situation"][:50]}...'
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Импорт завершен. Создано {created_count} новых записей из {len(business_values_data)}'
            )
        )

    def determine_category(self, business_value_text):
        """Определяет категорию на основе текста бизнес-ценности"""
        text_lower = business_value_text.lower()
        
        if 'компетентность' in text_lower:
            return 'competence'
        elif 'лидерство' in text_lower:
            return 'leadership'
        elif 'уникальность' in text_lower:
            return 'uniqueness'
        elif 'команда' in text_lower:
            return 'team'
        elif 'эспрессо культура' in text_lower:
            return 'espresso_culture'
        else:
            # Если категория не определена, используем компетентность по умолчанию
            return 'competence'

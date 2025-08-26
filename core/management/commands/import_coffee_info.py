from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import CoffeeInfo
import csv
import os
import re


class Command(BaseCommand):
    help = 'Импортирует информацию о кофе из очищенного CSV файла'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед импортом'
        )

    def handle(self, *args, **options):
        if options['clear']:
            CoffeeInfo.objects.all().delete()
            self.stdout.write('Существующая информация о кофе удалена')

        csv_file = 'data/processed/final_coffee_info_data.csv'
        
        if not os.path.exists(csv_file):
            self.stdout.write(
                self.style.ERROR(f'Файл не найден: {csv_file}')
            )
            return

        created_count = 0
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    title = row.get('title', '').strip()
                    content = row.get('content', '').strip()
                    filename = row.get('filename', '').strip()
                    
                    if not title or not content:
                        self.stdout.write(
                            self.style.WARNING(f'Пропущена строка с пустым заголовком или контентом')
                        )
                        continue
                    
                    # Определяем категорию
                    category = self.parse_category_info(title)
                    
                    # Очищаем и форматируем контент
                    clean_content = self.clean_and_format_content(content)
                    
                    # Создаем или обновляем запись
                    coffee_info, created = CoffeeInfo.objects.get_or_create(
                        title=title,
                        defaults={
                            'category': category,
                            'content': clean_content,
                            'order': 1,
                            'is_active': True
                        }
                    )
                    
                    if created:
                        self.stdout.write(
                            f'✅ Создана информация о кофе: {title}'
                        )
                        created_count += 1
                    else:
                        # Обновляем существующую запись
                        coffee_info.category = category
                        coffee_info.content = clean_content
                        coffee_info.save()
                        self.stdout.write(
                            f'🔄 Обновлена информация о кофе: {title}'
                        )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Ошибка при импорте: {e}')
            )
            return

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Импорт завершен. Создано {created_count} новых записей'
            )
        )

    def parse_category_info(self, title):
        """Определяет категорию из заголовка"""
        title_lower = title.lower()
        
        if 'зерн' in title_lower or 'боб' in title_lower:
            return 'beans'
        elif 'маркировк' in title_lower or 'классик' in title_lower or 'сорт' in title_lower:
            return 'varieties'
        elif 'экстракц' in title_lower or 'завариван' in title_lower or 'приготовлен' in title_lower:
            return 'brewing'
        elif 'качеств' in title_lower or 'дефект' in title_lower:
            return 'quality'
        else:
            return 'general'

    def clean_and_format_content(self, content):
        """Очищает и форматирует контент"""
        if not content:
            return ''
        
        # Убираем лишние пробелы и переносы строк
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = re.sub(r' +', ' ', content)
        
        # Убираем лишние пробелы в начале и конце
        content = content.strip()
        
        # Заменяем простые переносы строк на HTML теги
        lines = content.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Если строка похожа на заголовок (начинается с цифры и точки)
                if re.match(r'^\d+\.', line):
                    formatted_lines.append(f'<h3>{line}</h3>')
                # Если строка содержит маркированный список
                elif line.startswith('•'):
                    formatted_lines.append(f'<li>{line[1:].strip()}</li>')
                else:
                    formatted_lines.append(f'<p>{line}</p>')
        
        return '\n'.join(formatted_lines)

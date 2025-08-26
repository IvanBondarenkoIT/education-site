from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import TrainingProgram
import csv
import os
import re


class Command(BaseCommand):
    help = 'Импортирует программу обучения из очищенного CSV файла'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед импортом'
        )

    def handle(self, *args, **options):
        if options['clear']:
            TrainingProgram.objects.all().delete()
            self.stdout.write('Существующие программы обучения удалены')

        csv_file = 'data/processed/final_training_program_data.csv'
        
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
                    
                    # Определяем тип периода и номер
                    period_type, period_number = self.parse_period_info(title)
                    
                    # Очищаем и форматируем контент
                    clean_content = self.clean_and_format_content(content)
                    
                    # Создаем или обновляем запись
                    training_program, created = TrainingProgram.objects.get_or_create(
                        title=title,
                        defaults={
                            'period_type': period_type,
                            'period_number': period_number,
                            'content': clean_content,
                            'order': period_number,
                            'is_active': True
                        }
                    )
                    
                    if created:
                        self.stdout.write(
                            f'✅ Создана программа обучения: {title}'
                        )
                        created_count += 1
                    else:
                        # Обновляем существующую запись
                        training_program.period_type = period_type
                        training_program.period_number = period_number
                        training_program.content = clean_content
                        training_program.save()
                        self.stdout.write(
                            f'🔄 Обновлена программа обучения: {title}'
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

    def parse_period_info(self, title):
        """Определяет тип периода и номер из заголовка"""
        title_lower = title.lower()
        
        if 'день' in title_lower:
            # Извлекаем номер дня
            day_match = re.search(r'(\d+)\s*день', title_lower)
            if day_match:
                return 'day', int(day_match.group(1))
            return 'day', 1
        
        elif 'недели' in title_lower:
            # Извлекаем номер недели
            week_match = re.search(r'(\d+)\s*недели', title_lower)
            if week_match:
                return 'week', int(week_match.group(1))
            return 'week', 1
        
        elif 'месяца' in title_lower:
            # Извлекаем номер месяца
            month_match = re.search(r'(\d+)\s*месяца', title_lower)
            if month_match:
                return 'month', int(month_match.group(1))
            return 'month', 1
        
        else:
            # Дополнительные материалы
            return 'month', 99

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

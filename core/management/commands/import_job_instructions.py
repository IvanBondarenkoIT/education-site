from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import JobInstruction
import csv
import os
import re


class Command(BaseCommand):
    help = 'Импортирует должностные инструкции из очищенного CSV файла'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед импортом'
        )

    def handle(self, *args, **options):
        if options['clear']:
            JobInstruction.objects.all().delete()
            self.stdout.write('Существующие должностные инструкции удалены')

        csv_file = 'data/processed/final_job_instruction_data.csv'
        
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
                    
                    # Определяем должность и отдел
                    position, department = self.parse_position_info(title)
                    
                    # Очищаем и форматируем контент
                    clean_content = self.clean_and_format_content(content)
                    
                    # Создаем или обновляем запись
                    job_instruction, created = JobInstruction.objects.get_or_create(
                        title=title,
                        defaults={
                            'position': position,
                            'department': department,
                            'content': clean_content,
                            'order': 1,
                            'is_active': True
                        }
                    )
                    
                    if created:
                        self.stdout.write(
                            f'✅ Создана должностная инструкция: {title}'
                        )
                        created_count += 1
                    else:
                        # Обновляем существующую запись
                        job_instruction.position = position
                        job_instruction.department = department
                        job_instruction.content = clean_content
                        job_instruction.save()
                        self.stdout.write(
                            f'🔄 Обновлена должностная инструкция: {title}'
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

    def parse_position_info(self, title):
        """Определяет должность и отдел из заголовка"""
        title_lower = title.lower()
        
        # Определяем должность
        if 'менеджер' in title_lower:
            position = 'manager'
        elif 'бариста' in title_lower or 'саломе' in title_lower:
            position = 'barista'
        else:
            position = 'employee'
        
        # Определяем отдел
        if 'магазин' in title_lower or 'horeca' in title_lower or 'онлайн' in title_lower:
            department = 'retail'
        elif 'сервис' in title_lower:
            department = 'service'
        elif 'офис' in title_lower or 'консультант' in title_lower:
            department = 'office'
        else:
            department = 'general'
        
        return position, department

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

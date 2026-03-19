"""
Синхронизация контента из content/ (Markdown) в БД, затем экспорт в fixtures.

Использование:
  python manage.py sync_content_from_md              # content/ → DB → all_data.json
  python manage.py sync_content_from_md --no-export  # только content/ → DB

После sync_content_from_md:
  python manage.py loaddata all_data   # локально для проверки
  git add core/fixtures/all_data.json && git commit -m "Update content"
  git push   # для деплоя на Railway
"""
import re
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo


CATEGORY_MAP = {
    'Компетентность': 'competence',
    'Лидерство': 'leadership',
    'Уникальность': 'uniqueness',
    'Команда': 'team',
    'Эспрессо культура': 'espresso_culture',
}

PERIOD_MAP = {'День': 'day', 'Неделя': 'week', 'Месяц': 'month'}


class Command(BaseCommand):
    help = 'Синхронизирует контент из content/ в БД и экспортирует в fixtures'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-export',
            action='store_true',
            help='Не экспортировать в fixtures после синхронизации',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить контент-модели перед синхронизацией (рекомендуется при первом sync)',
        )
        parser.add_argument(
            '--content-dir',
            type=str,
            default='content',
            help='Путь к директории content/',
        )

    def handle(self, *args, **options):
        base = Path().resolve()
        content_dir = base / options['content_dir']

        if not content_dir.exists():
            self.stdout.write(self.style.ERROR(f'Директория не найдена: {content_dir}'))
            return

        if options['clear']:
            self.stdout.write('Очистка контент-моделей...')
            BusinessValue.objects.all().delete()
            TrainingProgram.objects.all().delete()
            JobInstruction.objects.all().delete()
            CoffeeInfo.objects.all().delete()
            self.stdout.write('  Удалено.')

        self.stdout.write('Синхронизация content/ -> БД...')

        self.sync_business_values(content_dir)
        self.sync_training_program(content_dir)
        self.sync_job_instructions(content_dir)
        self.sync_coffee_info(content_dir)

        if not options['no_export']:
            self.stdout.write('\nЭкспорт в fixtures...')
            call_command('export_fixtures', '--clear')
            self.stdout.write(self.style.SUCCESS('\n[OK] Контент синхронизирован и экспортирован в core/fixtures/all_data.json'))
            self.stdout.write('Далее: python manage.py loaddata all_data')
        else:
            self.stdout.write(self.style.SUCCESS('\n[OK] Контент синхронизирован в БД'))

    def sync_business_values(self, content_dir):
        path = content_dir / 'business_values.md'
        if not path.exists():
            return
        text = path.read_text(encoding='utf-8')

        # Парсим: ## Category, ### N. Situation, **Ценность:** value
        category = None
        order_in_cat = 0
        created = 0

        for block in re.split(r'\n(?=## |### )', text):
            block = block.strip()
            if not block:
                continue
            if block.startswith('## ') and not block.startswith('### '):
                cat_name = block.split('\n')[0].replace('## ', '').strip()
                category = CATEGORY_MAP.get(cat_name)
                order_in_cat = 0
                continue
            if block.startswith('### '):
                lines = block.split('\n')
                first = lines[0].replace('### ', '').strip()
                m = re.match(r'^\d+\.\s*(.+)', first)
                situation = m.group(1) if m else first
                value = ''
                for line in lines[1:]:
                    if line.strip().startswith('**Ценность:**'):
                        value = re.sub(r'\*\*Ценность:\*\*\s*', '', line).strip()
                        break
                if category and situation:
                    obj, is_new = BusinessValue.objects.update_or_create(
                        situation=situation,
                        category=category,
                        defaults={
                            'business_value': value,
                            'order': order_in_cat,
                            'is_active': True,
                        },
                    )
                    if is_new:
                        created += 1
                    order_in_cat += 1

        self.stdout.write(f'  BusinessValue: обновлено (создано новых: {created})')

    def sync_training_program(self, content_dir):
        path = content_dir / 'training_program.md'
        if not path.exists():
            return
        text = path.read_text(encoding='utf-8')

        # ## День 1: 1 день -> period_type=day, period_number=1
        for m in re.finditer(
            r'## (День|Неделя|Месяц) (\d+): ([^\n]+)\n\n([\s\S]*?)(?=\n---\n|\n## |\Z)',
            text,
        ):
            period_name, num, title, content = m.group(1), int(m.group(2)), m.group(3).strip(), m.group(4).strip()
            period_type = PERIOD_MAP.get(period_name, 'day')
            # Конвертируем markdown списки обратно в HTML-подобный текст
            content_clean = re.sub(r'^- ', '• ', content)
            content_clean = re.sub(r'\n- ', ' • ', content_clean)
            content_clean = content_clean.replace('\n\n', ' ').strip()
            content_html = f'<p>{content_clean}</p>'

            TrainingProgram.objects.update_or_create(
                period_type=period_type,
                period_number=num,
                defaults={
                    'title': title,
                    'content': content_html,
                    'order': num,
                    'is_active': True,
                },
            )
        self.stdout.write('  TrainingProgram: обновлено')

    def sync_job_instructions(self, content_dir):
        path = content_dir / 'job_instructions.md'
        if not path.exists():
            return
        text = path.read_text(encoding='utf-8')

        for m in re.finditer(
            r'## ([^\n]+)\n\n\*Должность:\s*([^|]+)\s*\|\s*Отдел:\s*([^*]+)\*\n\n([\s\S]*?)(?=\n---\n|\n## |\Z)',
            text,
        ):
            title, position, department, content = m.group(1).strip(), m.group(2).strip().lower(), m.group(3).strip().lower(), m.group(4).strip()
            content_clean = re.sub(r'^- ', '• ', content)
            content_clean = re.sub(r'\n- ', ' • ', content_clean)
            content_html = f'<p>{content_clean}</p>'

            # Маппинг для значений, которых может не быть в модели
            pos_map = {'barista': 'barista', 'employee': 'barista', 'manager': 'manager'}
            dept_map = {'general': 'barista', 'office': 'management', 'retail': 'management', 'service': 'management'}
            position = pos_map.get(position, 'barista')
            department = dept_map.get(department, 'barista')

            JobInstruction.objects.update_or_create(
                title=title[:180],
                defaults={
                    'position': position,
                    'department': department,
                    'content': content_html,
                    'is_active': True,
                },
            )
        self.stdout.write('  JobInstruction: обновлено')

    def sync_coffee_info(self, content_dir):
        path = content_dir / 'coffee_info.md'
        if not path.exists():
            return
        text = path.read_text(encoding='utf-8')

        for m in re.finditer(
            r'## ([^\n]+)\n\n\*Категория: ([^*]+)\*\n\n([\s\S]*?)(?=\n---\n|\n## |\Z)',
            text,
        ):
            title, category, content = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            cat_map = {'general': 'beans', 'brewing': 'brewing', 'varieties': 'varieties', 'beans': 'beans'}
            category = cat_map.get(category.lower(), category) if isinstance(category, str) else 'beans'
            content_clean = re.sub(r'^- ', '• ', content)
            content_clean = re.sub(r'\n- ', ' • ', content_clean)
            content_html = f'<p>{content_clean}</p>'

            CoffeeInfo.objects.update_or_create(
                title=title[:180],
                defaults={
                    'category': category,
                    'content': content_html,
                    'is_active': True,
                },
            )
        self.stdout.write('  CoffeeInfo: обновлено')

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from pathlib import Path


class Command(BaseCommand):
    help = 'Импортирует все данные из HTML файлов в папке source'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед импортом'
        )
        parser.add_argument(
            '--skip-business-values',
            action='store_true',
            help='Пропустить импорт бизнес-ценностей'
        )
        parser.add_argument(
            '--skip-training',
            action='store_true',
            help='Пропустить импорт программы обучения'
        )
        parser.add_argument(
            '--skip-instructions',
            action='store_true',
            help='Пропустить импорт должностных инструкций'
        )
        parser.add_argument(
            '--skip-coffee',
            action='store_true',
            help='Пропустить импорт информации о кофе'
        )

    def handle(self, *args, **options):
        self.stdout.write('Начинаем импорт всех данных...')
        
        # Импорт бизнес-ценностей
        if not options['skip_business_values']:
            self.stdout.write('\n1. Импорт бизнес-ценностей...')
            try:
                call_command('import_business_values', clear=options['clear'])
                self.stdout.write(self.style.SUCCESS('✓ Бизнес-ценности импортированы'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Ошибка импорта бизнес-ценностей: {e}'))
        else:
            self.stdout.write('⏭ Пропущен импорт бизнес-ценностей')

        # Импорт программы обучения
        if not options['skip_training']:
            self.stdout.write('\n2. Импорт программы обучения...')
            try:
                call_command('import_training_program', clear=options['clear'])
                self.stdout.write(self.style.SUCCESS('✓ Программа обучения импортирована'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Ошибка импорта программы обучения: {e}'))
        else:
            self.stdout.write('⏭ Пропущен импорт программы обучения')

        # Импорт должностных инструкций
        if not options['skip_instructions']:
            self.stdout.write('\n3. Импорт должностных инструкций...')
            try:
                call_command('import_job_instructions', clear=options['clear'])
                self.stdout.write(self.style.SUCCESS('✓ Должностные инструкции импортированы'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Ошибка импорта должностных инструкций: {e}'))
        else:
            self.stdout.write('⏭ Пропущен импорт должностных инструкций')

        # Импорт информации о кофе
        if not options['skip_coffee']:
            self.stdout.write('\n4. Импорт информации о кофе...')
            try:
                call_command('import_coffee_info', clear=options['clear'])
                self.stdout.write(self.style.SUCCESS('✓ Информация о кофе импортирована'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Ошибка импорта информации о кофе: {e}'))
        else:
            self.stdout.write('⏭ Пропущен импорт информации о кофе')

        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS('Импорт всех данных завершен!'))
        self.stdout.write('='*50)
        
        # Выводим статистику
        self.print_statistics()
        
        # Создаем фикстуры для будущего использования
        self.stdout.write('\n📦 Создаем фикстуры из импортированных данных...')
        try:
            call_command('export_fixtures', clear=True)
            self.stdout.write(self.style.SUCCESS('✅ Фикстуры созданы!'))
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Не удалось создать фикстуры: {e}')
            )
        
        self.stdout.write('\nТеперь вы можете:')
        self.stdout.write('1. Зайти в админку: http://127.0.0.1:8000/admin/')
        self.stdout.write('2. Просмотреть и отредактировать импортированные данные')
        self.stdout.write('3. Добавить переводы для многоязычности')
        self.stdout.write('4. Перейти к созданию views и templates')

    def print_statistics(self):
        """Выводит статистику импортированных данных"""
        from core.models import BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write('СТАТИСТИКА ИМПОРТА:')
        self.stdout.write('='*50)
        
        models = [
            ('Бизнес-ценности', BusinessValue),
            ('Программы обучения', TrainingProgram),
            ('Должностные инструкции', JobInstruction),
            ('Информация о кофе', CoffeeInfo),
        ]
        
        total_records = 0
        for name, model in models:
            count = model.objects.count()
            total_records += count
            status = '✅' if count > 0 else '❌'
            self.stdout.write(f'{status} {name}: {count} записей')
        
        self.stdout.write('='*50)
        self.stdout.write(f'ИТОГО: {total_records} записей')
        self.stdout.write('='*50)
        
        if total_records >= 55:  # Ожидаем минимум 55 записей
            self.stdout.write(
                self.style.SUCCESS('🎉 Импорт прошел успешно!')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Ожидалось больше записей, импортировано {total_records}')
            )

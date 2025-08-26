from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


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
        from core.models import BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo
        
        self.stdout.write('\nСтатистика:')
        self.stdout.write(f'• Бизнес-ценности: {BusinessValue.objects.count()}')
        self.stdout.write(f'• Программы обучения: {TrainingProgram.objects.count()}')
        self.stdout.write(f'• Должностные инструкции: {JobInstruction.objects.count()}')
        self.stdout.write(f'• Информация о кофе: {CoffeeInfo.objects.count()}')
        
        self.stdout.write('\nТеперь вы можете:')
        self.stdout.write('1. Зайти в админку: http://127.0.0.1:8000/admin/')
        self.stdout.write('2. Просмотреть и отредактировать импортированные данные')
        self.stdout.write('3. Добавить переводы для многоязычности')
        self.stdout.write('4. Перейти к созданию views и templates')

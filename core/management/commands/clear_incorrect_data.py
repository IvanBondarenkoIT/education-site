from django.core.management.base import BaseCommand
from core.models import TrainingProgram, JobInstruction, CoffeeInfo


class Command(BaseCommand):
    help = 'Очищает неправильные данные из моделей TrainingProgram, JobInstruction, CoffeeInfo'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Подтвердить удаление данных',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(
                    '⚠️  ВНИМАНИЕ: Эта команда удалит все данные из моделей TrainingProgram, JobInstruction, CoffeeInfo!'
                )
            )
            self.stdout.write(
                self.style.WARNING(
                    'Для подтверждения используйте --confirm'
                )
            )
            return

        # Подсчитываем количество записей перед удалением
        training_count = TrainingProgram.objects.count()
        job_count = JobInstruction.objects.count()
        coffee_count = CoffeeInfo.objects.count()

        self.stdout.write(f'📊 Текущее количество записей:')
        self.stdout.write(f'   TrainingProgram: {training_count}')
        self.stdout.write(f'   JobInstruction: {job_count}')
        self.stdout.write(f'   CoffeeInfo: {coffee_count}')

        # Удаляем данные
        TrainingProgram.objects.all().delete()
        JobInstruction.objects.all().delete()
        CoffeeInfo.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Данные успешно очищены!'
            )
        )
        self.stdout.write(f'   Удалено записей TrainingProgram: {training_count}')
        self.stdout.write(f'   Удалено записей JobInstruction: {job_count}')
        self.stdout.write(f'   Удалено записей CoffeeInfo: {coffee_count}')
        
        self.stdout.write(
            self.style.SUCCESS(
                'Теперь можно импортировать правильные данные с помощью команд:'
            )
        )
        self.stdout.write('   python manage.py import_training_program')
        self.stdout.write('   python manage.py import_job_instructions')
        self.stdout.write('   python manage.py import_coffee_info')


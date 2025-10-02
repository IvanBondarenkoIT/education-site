from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.serializers import serialize
from core.models import Language, BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo
import os
import json
from pathlib import Path


class Command(BaseCommand):
    help = 'Экспортирует все данные в JSON фикстуры для деплоя'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output-dir',
            type=str,
            default='core/fixtures',
            help='Директория для сохранения фикстур'
        )
        parser.add_argument(
            '--separate-files',
            action='store_true',
            help='Создать отдельные файлы для каждой модели'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие фикстуры перед экспортом'
        )

    def handle(self, *args, **options):
        output_dir = Path(options['output_dir'])
        separate_files = options['separate_files']
        clear = options['clear']

        # Создаем директорию если не существует
        output_dir.mkdir(parents=True, exist_ok=True)

        if clear:
            # Удаляем существующие фикстуры
            for fixture_file in output_dir.glob('*.json'):
                fixture_file.unlink()
                self.stdout.write(f'Удален файл: {fixture_file}')

        self.stdout.write('Начинаем экспорт данных в фикстуры...')

        # Экспортируем языки
        languages = Language.objects.all()
        if languages.exists():
            self.export_model_data(languages, 'languages', output_dir, separate_files)

        # Экспортируем бизнес-ценности
        business_values = BusinessValue.objects.all()
        if business_values.exists():
            self.export_model_data(business_values, 'business_values', output_dir, separate_files)

        # Экспортируем программы обучения
        training_programs = TrainingProgram.objects.all()
        if training_programs.exists():
            self.export_model_data(training_programs, 'training_programs', output_dir, separate_files)

        # Экспортируем должностные инструкции
        job_instructions = JobInstruction.objects.all()
        if job_instructions.exists():
            self.export_model_data(job_instructions, 'job_instructions', output_dir, separate_files)

        # Экспортируем информацию о кофе
        coffee_info = CoffeeInfo.objects.all()
        if coffee_info.exists():
            self.export_model_data(coffee_info, 'coffee_info', output_dir, separate_files)

        # Создаем общий файл со всеми данными
        if not separate_files:
            self.create_all_data_fixture(output_dir)

        # Выводим статистику
        self.print_statistics()

        self.stdout.write(
            self.style.SUCCESS('[OK] Экспорт фикстур завершен успешно!')
        )

    def export_model_data(self, queryset, model_name, output_dir, separate_files):
        """Экспортирует данные модели в JSON фикстуру"""
        if not queryset.exists():
            self.stdout.write(
                self.style.WARNING(f'⚠️  Нет данных для модели {model_name}')
            )
            return

        # Сериализуем данные
        serialized_data = serialize('json', queryset, indent=2)
        
        # Парсим JSON для красивого форматирования
        data = json.loads(serialized_data)
        
        if separate_files:
            # Создаем отдельный файл для модели
            fixture_file = output_dir / f'{model_name}.json'
            with open(fixture_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            self.stdout.write(
                f'[OK] Создан файл: {fixture_file} ({len(data)} записей)'
            )
        
        return data

    def create_all_data_fixture(self, output_dir):
        """Создает общий файл со всеми данными"""
        all_data = []
        
        # Собираем данные из всех моделей
        models_data = [
            ('languages', Language.objects.all()),
            ('business_values', BusinessValue.objects.all()),
            ('training_programs', TrainingProgram.objects.all()),
            ('job_instructions', JobInstruction.objects.all()),
            ('coffee_info', CoffeeInfo.objects.all()),
        ]
        
        for model_name, queryset in models_data:
            if queryset.exists():
                serialized = serialize('json', queryset)
                data = json.loads(serialized)
                all_data.extend(data)
                self.stdout.write(f'[OK] Добавлены {queryset.count()} записей из {model_name}')
        
        # Сохраняем общий файл
        all_data_file = output_dir / 'all_data.json'
        with open(all_data_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        self.stdout.write(
            f'[OK] Создан общий файл: {all_data_file} ({len(all_data)} записей)'
        )

    def print_statistics(self):
        """Выводит статистику экспортированных данных"""
        self.stdout.write('\n' + '='*50)
        self.stdout.write('СТАТИСТИКА ЭКСПОРТА:')
        self.stdout.write('='*50)
        
        models = [
            ('Languages', Language),
            ('Business Values', BusinessValue),
            ('Training Programs', TrainingProgram),
            ('Job Instructions', JobInstruction),
            ('Coffee Info', CoffeeInfo),
        ]
        
        total_records = 0
        for name, model in models:
            count = model.objects.count()
            total_records += count
            self.stdout.write(f'• {name}: {count} записей')
        
        self.stdout.write('='*50)
        self.stdout.write(f'ИТОГО: {total_records} записей')
        self.stdout.write('='*50)
        
        self.stdout.write('\nФайлы фикстур созданы в: core/fixtures/')
        self.stdout.write('Теперь можно использовать: python manage.py loaddata all_data')

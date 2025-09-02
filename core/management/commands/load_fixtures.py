from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Загружает данные из фикстур с fallback на импорт из файлов'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить существующие данные перед загрузкой'
        )
        parser.add_argument(
            '--fixtures-dir',
            type=str,
            default='core/fixtures',
            help='Директория с фикстурами'
        )
        parser.add_argument(
            '--fallback',
            action='store_true',
            help='Использовать fallback импорт если фикстуры не найдены'
        )

    def handle(self, *args, **options):
        clear = options['clear']
        fixtures_dir = Path(options['fixtures_dir'])
        fallback = options['fallback']

        self.stdout.write('Начинаем загрузку данных из фикстур...')

        # Проверяем наличие фикстур
        all_data_fixture = fixtures_dir / 'all_data.json'
        
        if all_data_fixture.exists():
            self.stdout.write(f'✅ Найдена фикстура: {all_data_fixture}')
            
            # Очищаем данные если нужно
            if clear:
                self.clear_all_data()
            
            # Загружаем данные из фикстуры
            try:
                call_command('loaddata', 'all_data', verbosity=0)
                self.stdout.write(
                    self.style.SUCCESS('✅ Данные успешно загружены из фикстуры!')
                )
                
                # Показываем статистику
                self.print_statistics()
                return
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Ошибка загрузки фикстуры: {e}')
                )
                if not fallback:
                    return
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Фикстура не найдена: {all_data_fixture}')
            )
            if not fallback:
                self.stdout.write(
                    self.style.ERROR('❌ Fallback отключен. Создайте фикстуры командой: python manage.py export_fixtures')
                )
                return

        # Fallback: импорт из файлов
        if fallback:
            self.stdout.write('\n🔄 Запускаем fallback импорт из файлов...')
            try:
                call_command('import_all_data', clear=clear)
                self.stdout.write(
                    self.style.SUCCESS('✅ Fallback импорт завершен успешно!')
                )
                
                # Показываем статистику
                self.print_statistics()
                
                # Создаем фикстуры для будущего использования
                self.stdout.write('\n📦 Создаем фикстуры из импортированных данных...')
                call_command('export_fixtures', clear=True)
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Ошибка fallback импорта: {e}')
                )
                self.show_manual_instructions()

    def clear_all_data(self):
        """Очищает все данные из моделей"""
        from core.models import Language, BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo
        
        self.stdout.write('🗑️  Очищаем существующие данные...')
        
        models = [Language, BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo]
        
        for model in models:
            count = model.objects.count()
            if count > 0:
                model.objects.all().delete()
                self.stdout.write(f'✅ Очищено {count} записей из {model.__name__}')

    def print_statistics(self):
        """Выводит статистику загруженных данных"""
        from core.models import Language, BusinessValue, TrainingProgram, JobInstruction, CoffeeInfo
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write('СТАТИСТИКА ЗАГРУЖЕННЫХ ДАННЫХ:')
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
            status = '✅' if count > 0 else '❌'
            self.stdout.write(f'{status} {name}: {count} записей')
        
        self.stdout.write('='*50)
        self.stdout.write(f'ИТОГО: {total_records} записей')
        self.stdout.write('='*50)
        
        if total_records == 59:
            self.stdout.write(
                self.style.SUCCESS('🎉 Все данные загружены корректно!')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️  Ожидалось 59 записей, загружено {total_records}')
            )

    def show_manual_instructions(self):
        """Показывает инструкции по ручной настройке"""
        self.stdout.write('\n' + '='*60)
        self.stdout.write('📋 ИНСТРУКЦИИ ПО РУЧНОЙ НАСТРОЙКЕ:')
        self.stdout.write('='*60)
        
        self.stdout.write('\n1. Убедитесь что данные импортированы:')
        self.stdout.write('   python manage.py import_all_data')
        
        self.stdout.write('\n2. Создайте фикстуры:')
        self.stdout.write('   python manage.py export_fixtures')
        
        self.stdout.write('\n3. Проверьте что фикстуры созданы:')
        self.stdout.write('   ls core/fixtures/')
        
        self.stdout.write('\n4. Протестируйте загрузку фикстур:')
        self.stdout.write('   python manage.py load_fixtures')
        
        self.stdout.write('\n5. Проверьте данные в админке:')
        self.stdout.write('   http://127.0.0.1:8000/admin/')
        
        self.stdout.write('='*60)

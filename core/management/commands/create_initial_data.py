from django.core.management.base import BaseCommand
from core.models import Language


class Command(BaseCommand):
    help = 'Создает начальные данные для сайта'

    def handle(self, *args, **options):
        self.stdout.write('Создание начальных данных...')
        
        # Создаем языки
        languages_data = [
            {
                'code': 'ru',
                'name': 'Русский',
                'flag_icon': '🇷🇺',
                'is_active': True,
                'is_default': True,
                'order': 1
            },
            {
                'code': 'uk',
                'name': 'Українська',
                'flag_icon': '🇺🇦',
                'is_active': True,
                'is_default': False,
                'order': 2
            },
            {
                'code': 'en',
                'name': 'English',
                'flag_icon': '🇬🇧',
                'is_active': True,
                'is_default': False,
                'order': 3
            },
            {
                'code': 'ge',
                'name': 'ქართული',
                'flag_icon': '🇬🇪',
                'is_active': True,
                'is_default': False,
                'order': 4
            }
        ]
        
        for lang_data in languages_data:
            language, created = Language.objects.get_or_create(
                code=lang_data['code'],
                defaults=lang_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Создан язык: {language.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Язык уже существует: {language.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Начальные данные созданы успешно!')
        )

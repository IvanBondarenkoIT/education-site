"""
Создаёт суперпользователя для доступа к админке.
Используется для локальной разработки. В продакшене смените пароль!
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

# Данные по умолчанию (можно переопределить через переменные окружения)
DEFAULT_USERNAME = 'admin'
DEFAULT_EMAIL = 'admin@dimkava.local'
DEFAULT_PASSWORD = 'admin123'


class Command(BaseCommand):
    help = 'Создаёт суперпользователя admin/admin123 для доступа к админке (локальная разработка)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            default=None,
            help='Логин (по умолчанию: admin)',
        )
        parser.add_argument(
            '--password',
            default=None,
            help='Пароль (по умолчанию: admin123)',
        )
        parser.add_argument(
            '--email',
            default=None,
            help='Email (по умолчанию: admin@dimkava.local)',
        )

    def handle(self, *args, **options):
        import os
        from django.conf import settings

        username = options.get('username') or os.environ.get('ADMIN_USERNAME', DEFAULT_USERNAME)
        password = options.get('password') or os.environ.get('ADMIN_PASSWORD', DEFAULT_PASSWORD)
        email = options.get('email') or os.environ.get('ADMIN_EMAIL', DEFAULT_EMAIL)

        # В продакшене (DEBUG=False) требуем ADMIN_PASSWORD через переменные окружения
        if not settings.DEBUG and password == DEFAULT_PASSWORD:
            self.stdout.write(
                self.style.WARNING(
                    'Пропуск создания админа: в продакшене задайте ADMIN_PASSWORD в переменных окружения Railway.'
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Пользователь "{username}" уже существует.')
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Создан суперпользователь: {username} / {password}\n'
                f'Админка: http://127.0.0.1:8000/admin/'
            )
        )

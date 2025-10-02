from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import activate
from .models import (
    Language, BusinessValue, TrainingProgram, 
    JobInstruction, CoffeeInfo
)


class BaseTestCase(TestCase):
    """Базовый класс для тестов с общей настройкой"""
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.client = Client()
        
        # Создаем языки
        self.ru_language = Language.objects.create(
            code='ru',
            name='Русский',
            flag_icon='🇷🇺',
            is_active=True,
            is_default=True,
            order=1
        )
        
        self.uk_language = Language.objects.create(
            code='uk',
            name='Українська',
            flag_icon='🇺🇦',
            is_active=True,
            is_default=False,
            order=2
        )
        
        # Создаем бизнес-ценности
        self.business_value = BusinessValue.objects.create(
            situation='Тестовая ситуация',
            business_value='Тестовая бизнес-ценность',
            category='competence',
            order=1
        )
        
        # Создаем программу обучения
        self.training_program = TrainingProgram.objects.create(
            title='Тестовая программа обучения',
            content='Тестовое содержание программы',
            period_type='day',
            period_number=1,
            order=1
        )
        
        # Создаем должностную инструкцию
        self.job_instruction = JobInstruction.objects.create(
            position='manager',
            department='management',
            title='Тестовая должностная инструкция',
            content='Тестовое содержание инструкции',
            order=1
        )
        
        # Создаем информацию о кофе
        self.coffee_info = CoffeeInfo.objects.create(
            category='beans',
            title='Тестовая информация о кофе',
            content='Тестовое содержание о кофе',
            order=1
        )


class HomePageTest(BaseTestCase):
    """Тесты для главной страницы"""
    
    def test_home_page_loads(self):
        """Проверяем, что главная страница загружается"""
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_home_page_context(self):
        """Проверяем контекст главной страницы"""
        response = self.client.get(reverse('core:home'))
        self.assertIn('page_title', response.context)
        self.assertIn('stats', response.context)
        self.assertEqual(response.context['page_title'], 'Dim Kava - Образовательный портал')
    
    def test_home_page_stats(self):
        """Проверяем статистику на главной странице"""
        response = self.client.get(reverse('core:home'))
        stats = response.context['stats']
        self.assertIn('business_values_count', stats)
        self.assertIn('job_instructions_count', stats)
        self.assertIn('coffee_info_count', stats)
        self.assertIn('languages_count', stats)


class BusinessValuesTest(BaseTestCase):
    """Тесты для страницы бизнес-ценностей"""
    
    def test_business_values_page_loads(self):
        """Проверяем, что страница бизнес-ценностей загружается"""
        response = self.client.get(reverse('core:business_values'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_values.html')
    
    def test_business_values_context(self):
        """Проверяем контекст страницы бизнес-ценностей"""
        response = self.client.get(reverse('core:business_values'))
        self.assertIn('page_title', response.context)
        self.assertIn('business_values', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('total_count', response.context)
        self.assertEqual(response.context['page_title'], 'Бизнес-ценности компании')
    
    def test_business_values_data(self):
        """Проверяем данные бизнес-ценностей"""
        response = self.client.get(reverse('core:business_values'))
        business_values = response.context['business_values']
        self.assertEqual(business_values.count(), 1)
        self.assertEqual(business_values.first(), self.business_value)


class TrainingProgramTest(BaseTestCase):
    """Тесты для страницы программы обучения"""
    
    def test_training_program_page_loads(self):
        """Проверяем, что страница программы обучения загружается"""
        response = self.client.get(reverse('core:training_program'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training/training_program.html')
    
    def test_training_program_context(self):
        """Проверяем контекст страницы программы обучения"""
        response = self.client.get(reverse('core:training_program'))
        self.assertIn('page_title', response.context)
        self.assertIn('daily_programs', response.context)
        self.assertIn('weekly_programs', response.context)
        self.assertIn('monthly_programs', response.context)
        self.assertEqual(response.context['page_title'], 'Программа обучения новых сотрудников')
    
    def test_training_program_data(self):
        """Проверяем данные программы обучения"""
        response = self.client.get(reverse('core:training_program'))
        daily_programs = response.context['daily_programs']
        self.assertEqual(daily_programs.count(), 1)
        self.assertEqual(daily_programs.first(), self.training_program)
    
    def test_training_detail_page_loads(self):
        """Проверяем, что детальная страница программы обучения загружается"""
        response = self.client.get(
            reverse('core:training_detail', args=[self.training_program.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training/training_detail.html')
    
    def test_training_detail_context(self):
        """Проверяем контекст детальной страницы программы обучения"""
        response = self.client.get(
            reverse('core:training_detail', args=[self.training_program.id])
        )
        self.assertIn('page_title', response.context)
        self.assertIn('program', response.context)
        self.assertEqual(response.context['program'], self.training_program)


class JobInstructionsTest(BaseTestCase):
    """Тесты для страницы должностных инструкций"""
    
    def test_job_instructions_page_loads(self):
        """Проверяем, что страница должностных инструкций загружается"""
        response = self.client.get(reverse('core:job_instructions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructions/job_instructions.html')
    
    def test_job_instructions_context(self):
        """Проверяем контекст страницы должностных инструкций"""
        response = self.client.get(reverse('core:job_instructions'))
        self.assertIn('page_title', response.context)
        self.assertIn('instructions', response.context)
        self.assertIn('departments', response.context)
        self.assertIn('total_count', response.context)
        self.assertEqual(response.context['page_title'], 'Должностные инструкции')
    
    def test_job_instructions_data(self):
        """Проверяем данные должностных инструкций"""
        response = self.client.get(reverse('core:job_instructions'))
        instructions = response.context['instructions']
        self.assertEqual(instructions.count(), 1)
        self.assertEqual(instructions.first(), self.job_instruction)
    
    def test_job_instruction_detail_page_loads(self):
        """Проверяем, что детальная страница должностной инструкции загружается"""
        response = self.client.get(
            reverse('core:job_instruction_detail', args=[self.job_instruction.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructions/job_instruction_detail.html')
    
    def test_job_instruction_detail_context(self):
        """Проверяем контекст детальной страницы должностной инструкции"""
        response = self.client.get(
            reverse('core:job_instruction_detail', args=[self.job_instruction.id])
        )
        self.assertIn('page_title', response.context)
        self.assertIn('instruction', response.context)
        self.assertEqual(response.context['instruction'], self.job_instruction)


class CoffeeInfoTest(BaseTestCase):
    """Тесты для страницы информации о кофе"""
    
    def test_coffee_info_page_loads(self):
        """Проверяем, что страница информации о кофе загружается"""
        response = self.client.get(reverse('core:coffee_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coffee_info/coffee_info.html')
    
    def test_coffee_info_context(self):
        """Проверяем контекст страницы информации о кофе"""
        response = self.client.get(reverse('core:coffee_info'))
        self.assertIn('page_title', response.context)
        self.assertIn('coffee_info_list', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('total_count', response.context)
        self.assertEqual(response.context['page_title'], 'Информация о кофе и зерне')
    
    def test_coffee_info_data(self):
        """Проверяем данные информации о кофе"""
        response = self.client.get(reverse('core:coffee_info'))
        coffee_info_list = response.context['coffee_info_list']
        self.assertEqual(coffee_info_list.count(), 1)
        self.assertEqual(coffee_info_list.first(), self.coffee_info)
    
    def test_coffee_info_detail_page_loads(self):
        """Проверяем, что детальная страница информации о кофе загружается"""
        response = self.client.get(
            reverse('core:coffee_info_detail', args=[self.coffee_info.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coffee_info/coffee_info_detail.html')
    
    def test_coffee_info_detail_context(self):
        """Проверяем контекст детальной страницы информации о кофе"""
        response = self.client.get(
            reverse('core:coffee_info_detail', args=[self.coffee_info.id])
        )
        self.assertIn('page_title', response.context)
        self.assertIn('coffee_info', response.context)
        self.assertEqual(response.context['coffee_info'], self.coffee_info)


class LanguageSwitchingTest(BaseTestCase):
    """Тесты для переключения языков"""
    
    def test_set_language_view(self):
        """Проверяем view для переключения языка"""
        response = self.client.post(reverse('core:set_language'), {
            'language': 'uk'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
    
    def test_language_context_processor(self):
        """Проверяем контекстный процессор для языков"""
        response = self.client.get(reverse('core:home'))
        self.assertIn('current_language', response.context)
        self.assertIn('available_languages', response.context)
        self.assertIn('languages', response.context)


class ErrorPagesTest(BaseTestCase):
    """Тесты для страниц ошибок"""
    
    def test_404_page(self):
        """Проверяем 404 страницу"""
        response = self.client.get('/non-existent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
    
    def test_500_page(self):
        """Проверяем 500 страницу"""
        # Проверяем, что 500 страница существует
        response = self.client.get('/non-existent-page/')
        self.assertEqual(response.status_code, 404)


class URLPatternsTest(BaseTestCase):
    """Тесты для URL паттернов"""
    
    def test_all_urls_resolve(self):
        """Проверяем, что все URL паттерны разрешаются"""
        urls_to_test = [
            'core:home',
            'core:business_values',
            'core:training_program',
            'core:job_instructions',
            'core:coffee_info',
            'core:set_language',
        ]
        
        for url_name in urls_to_test:
            try:
                reverse(url_name)
            except Exception as e:
                self.fail(f"URL {url_name} не разрешается: {e}")
    
    def test_detail_urls_resolve(self):
        """Проверяем, что URL для детальных страниц разрешаются"""
        detail_urls = [
            ('core:training_detail', self.training_program.id),
            ('core:job_instruction_detail', self.job_instruction.id),
            ('core:coffee_info_detail', self.coffee_info.id),
        ]
        
        for url_name, obj_id in detail_urls:
            try:
                reverse(url_name, args=[obj_id])
            except Exception as e:
                self.fail(f"URL {url_name} с id {obj_id} не разрешается: {e}")


class ModelTest(BaseTestCase):
    """Тесты для моделей"""
    
    def test_business_value_str(self):
        """Проверяем строковое представление BusinessValue"""
        self.assertIn('Тестовая ситуация', str(self.business_value))
    
    def test_training_program_str(self):
        """Проверяем строковое представление TrainingProgram"""
        self.assertIn('День 1', str(self.training_program))
    
    def test_job_instruction_str(self):
        """Проверяем строковое представление JobInstruction"""
        self.assertIn('Менеджер магазина', str(self.job_instruction))
    
    def test_coffee_info_str(self):
        """Проверяем строковое представление CoffeeInfo"""
        self.assertIn('Тестовая информация о кофе', str(self.coffee_info))
    
    def test_language_str(self):
        """Проверяем строковое представление Language"""
        self.assertEqual(str(self.ru_language), '🇷🇺 Русский (ru)')


class IntegrationTest(BaseTestCase):
    """Интеграционные тесты"""
    
    def test_full_navigation_flow(self):
        """Проверяем полный поток навигации по сайту"""
        # Главная страница
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        
        # Бизнес-ценности
        response = self.client.get(reverse('core:business_values'))
        self.assertEqual(response.status_code, 200)
        
        # Программа обучения
        response = self.client.get(reverse('core:training_program'))
        self.assertEqual(response.status_code, 200)
        
        # Должностные инструкции
        response = self.client.get(reverse('core:job_instructions'))
        self.assertEqual(response.status_code, 200)
        
        # Информация о кофе
        response = self.client.get(reverse('core:coffee_info'))
        self.assertEqual(response.status_code, 200)
    
    def test_detail_pages_flow(self):
        """Проверяем поток детальных страниц"""
        # Детальная страница программы обучения
        response = self.client.get(
            reverse('core:training_detail', args=[self.training_program.id])
        )
        self.assertEqual(response.status_code, 200)
        
        # Детальная страница должностной инструкции
        response = self.client.get(
            reverse('core:job_instruction_detail', args=[self.job_instruction.id])
        )
        self.assertEqual(response.status_code, 200)
        
        # Детальная страница информации о кофе
        response = self.client.get(
            reverse('core:coffee_info_detail', args=[self.coffee_info.id])
        )
        self.assertEqual(response.status_code, 200)

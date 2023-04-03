from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from feedback.models import FeedBack

User = get_user_model()


class StaticURLTests(TestCase):
    def test_homepage(self):
        # Создаем экземпляр клиента
        guest_client = Client()
        # Делаем запрос к главной странице и проверяем статус
        response = guest_client.get('/')
        # Утверждаем, что для прохождения теста код должен быть равен 200
        self.assertEqual(response.status_code, 200)


# пример теста на проверку доступности адреса и на совпадение шаблона
# простым способом - без subTests
class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_availability_page_about(self):
        response = self.guest_client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_availability_template_about(self):
        response = self.guest_client.get('/about/')
        self.assertTemplateUsed(response, 'about/about.html')


# тесты через subTests, проверяем разом несколько урлов
class URLTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()
        # Создаем пользователя
        self.user = User.objects.create_user(username='NoName')
        # Создаем второй клиент
        self.authorized_client = Client()
        # авторизуем его
        self.authorized_client.force_login(self.user)

    def test_correct_templates_registered_user(self):
        '''проверяем используется ли соответствующий
           шаблон зарегистрированным пользователем'''

        templates_url = {
            'bikes/index.html': '/',
            'bikes/brand_group.html': '/brand/test-brand/',
            'bikes/model_detail.html': '/brand/test-brand/test_model/',
            'bikes/format.html': '/veloformat/test-format/',
            'bikes/sex_age_group.html': '/for/test-sex-age/',
            'about/about.html': '/about/',
            'feedback/create.html': '/feedback/create/',
            'feedback/feedback.html': '/feedback/',
            'users/password_reset_form.html': '/auth/password_reset/',
        }
        for template, adress in templates_url.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(adress)
                self.assertTemplateUsed(response, template)

    def test_correct_templates_with_unregistered_user(self):
        '''проверяем используется ли соответствующий
           шаблон незарегистрированным пользователем'''

        templates_url = {
            'bikes/index.html': '/',
            'bikes/brand_group.html': '/brand/test-brand/',
            'bikes/model_detail.html': '/brand/test-brand/test_model/',
            'bikes/format.html': '/veloformat/test-format/',
            'bikes/sex_age_group.html': '/for/test-sex-age/',
            'about/about.html': '/about/',
            'feedback/feedback.html': '/feedback/',
            'users/signup.html': '/auth/signup/',
            'users/login.html': '/auth/login/',
            # 'users/logout.html': '/auth/logout/',
        }
        for template, adress in templates_url.items():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                self.assertTemplateUsed(response, template)


# пример теста на проверку доступности адреса
# class URLTests(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         return super().setUpClass()

#     def setUp(self):
#         # Создаем неавторизованный клиент
#         self.guest_client = Client()
#         # Создаем пользователя
#         self.user = User.objects.create_user(username='NoName')
#         # Создаем второй клиент
#         self.authorized_client = Client()
#         # авторизуем его
#         self.authorized_client.force_login(self.user)

#     def test_correct_templates_registered_user(self):
#         '''проверяем доступность адреса зарегистрированным пользователем'''

#         adress_url = [
#             '/',
#             '/brand/test-brand/',
#             '/brand/test-brand/test_model/',
#             '/veloformat/test-format/',
#             '/for/test-sex-age/',
#             '/about/',
#             '/feedback/create/',
#             '/feedback/',
#         ]
#         for adress in adress_url:
#             with self.subTest(adress=adress):
#                 response = self.authorized_client.get(adress)
#                 self.assertEqual(response.status_code, 200)

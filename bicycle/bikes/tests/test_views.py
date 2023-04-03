from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from feedback.models import FeedBack
from bikes.models import New_Bike

User = get_user_model()


class BikePagesTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # создаем тестовую запись в БД
        New_Bike.objects.create(
            brand='Best',
            model='Bike',
            sex_age='woman',
            veloformat='BMX',
            description='Just_text',
            price=5000,
            brand_slug='best',
            model_slug='bike',
        )

    def setUp(self):
        # Создаем авторизованный клиент
        self.user = User.objects.create_user(username='Noname')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_home_page_correct_template(self):
        """URL-адрес использует шаблон bikes/index.html."""
        response = self.authorized_client.get(reverse('bikes:index'))
        self.assertTemplateUsed(response, 'bikes/index.html')

    def test_task_veloformat_correct_template(self):
        """URL-адреса используют шаблон bikes/veloformat.html."""
        response = self.authorized_client.get(
            reverse('bikes:format', kwargs={'format': 'BMX'}))
        self.assertTemplateUsed(response, 'bikes/format.html')

    def test_task_brand_group_correct_template(self):
        """URL-адреса используют шаблон bikes/brand_group.html."""
        response = self.authorized_client.get(
            reverse('bikes:brand_group', kwargs={'brand_slug': 'best'}))
        self.assertTemplateUsed(response, 'bikes/brand_group.html')

from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *
from django.utils import timezone
from urllib.parse import urlencode


# Create your tests here.
class StatusmuUnitTest(TestCase):
    def test_statusmu_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_statusmu_page_contains_hello(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Hello Apa Kabar?</h1>')

    def test_statusmu_model_can_create_new_status(self):
        Statusmu.objects.create(name='test', status='hehe')
        count_status = Statusmu.objects.all().count()
        self.assertEqual(count_status, 1)

    def test_statusmu_can_add_status(self):
        data = urlencode({'name': 'huhu', 'status': 'hehe'})
        response = self.client.post(
            '/', data, content_type="application/x-www-form-urlencoded")
        count_status = Statusmu.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_status, 1)

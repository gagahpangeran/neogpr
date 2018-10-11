from django.test import TestCase, Client
from django.urls import resolve, reverse


# Create your tests here.
class StatusmuUnitTest(TestCase):
    def test_statusmu_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_statusmu_page_contains_hello(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Hello Apa Kabar?</h1>')

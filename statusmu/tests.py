from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *
from django.utils import timezone
from urllib.parse import urlencode
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


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

    def test_statusmu_get_right_data(self):
        data = urlencode({'name': 'aku', 'status': 'kamu'})
        response = self.client.post(
            '/', data, content_type="application/x-www-form-urlencoded")
        result = Statusmu.objects.first()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(result.name, 'aku')
        self.assertEquals(result.status, 'kamu')

    def test_profil_url_is_exist(self):
        response = Client().get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profil_page_contains_name(self):
        response = self.client.get('/profile/')
        self.assertContains(response, '<h1>Gagah Pangeran Rosfatiputra</h1>')


class StatusmuFunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.selenium = webdriver.Chrome(options=chrome_options)
        self.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        self.selenium.quit()
        super().tearDownClass()

    def test_statusmu_page_contain_hello(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        self.assertIn('Hello Apa Kabar?', selenium.page_source)

    def test_statusmu_add_status(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        self.assertNotIn('Coba Coba', selenium.page_source)

        name_field = selenium.find_element_by_id('name')
        status_field = selenium.find_element_by_id('status')
        submit_button = selenium.find_element_by_id('submit')

        name_field.send_keys('selenium')
        status_field.send_keys('Coba Coba')
        submit_button.click()

        self.assertIn('Coba Coba', selenium.page_source)

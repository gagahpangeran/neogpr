from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *
from django.utils import timezone
from urllib.parse import urlencode
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import requests


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

    def test_books_page_is_exist(self):
        response = Client().get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_books_page_can_get_data(self):
        response = Client().get('/api/books/')
        self.assertTrue(response is not None)

    def test_register_page_is_exist(self):
        response = Client().get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_not_exist_email(self):
        data = {'email': 'gpr@uwu.com'}
        response = self.client.post(
            '/api/check-email/', json.dumps(data), content_type='application/json')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), {'exist': False})

    def test_can_register_user(self):
        data = {'email': 'f@sil.com', 'name': 'GPR', 'password': '4dm1n'}
        response = self.client.post(
            '/api/register/', json.dumps(data), content_type='application/json')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), {'success': True})

        data['hehe'] = 'hehe'
        response = self.client.post(
            '/api/register/', json.dumps(data), content_type='application/json')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), {'success': False})

    def test_can_get_subscriber_list(self):
        response = Client().get('/api/list-subscriber/')
        self.assertTrue(response is not None)

    def test_can_delete_subscriber(self):
        response = self.client.get('/api/delete-subscriber/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), {'success': False})

        data = {'email': 'gpr@gpr.com', 'name': 'GPR', 'password': '4dm1n'}
        self.client.post(
            '/api/register/', json.dumps(data), content_type='application/json')

        data = {'id': 1}
        response = self.client.post(
            '/api/delete-subscriber/', json.dumps(data), content_type='application/json')

        self.assertJSONEqual(
            str(response.content, encoding='utf8'), {'success': True})


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

    def test_statusmu_add_status(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        time.sleep(5)

        self.assertNotIn('selenium', selenium.page_source)
        self.assertNotIn('Coba Coba', selenium.page_source)

        time.sleep(5)

        name_field = selenium.find_element_by_id('name')
        status_field = selenium.find_element_by_id('status')
        submit_button = selenium.find_element_by_id('submit')

        name_field.send_keys('selenium')
        status_field.send_keys('Coba Coba')
        submit_button.click()

        time.sleep(5)

        self.assertIn('selenium', selenium.page_source)
        self.assertIn('Coba Coba', selenium.page_source)

    def test_statusmu_add_anonim_status(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        time.sleep(5)

        self.assertNotIn('Anonim', selenium.page_source)
        self.assertNotIn('Hehe', selenium.page_source)

        time.sleep(5)

        status_field = selenium.find_element_by_id('status')
        submit_button = selenium.find_element_by_id('submit')

        status_field.send_keys('Hehe')
        submit_button.click()

        time.sleep(5)

        self.assertIn('Anonim', selenium.page_source)
        self.assertIn('Hehe', selenium.page_source)

    def test_statusmu_page_contain_hello(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        self.assertIn('<h1>Hello Apa Kabar?</h1>', selenium.page_source)

    def test_statusmu_page_contain_title(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        self.assertIn('<title>Gagah Pangeran Rosfatiputra</title>',
                      selenium.page_source)

    def test_page_background_color(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        background = selenium.find_element_by_id(
            'container').value_of_css_property('background-color')

        self.assertIn('rgba(176, 44, 40, 1)', background)

    def test_form_background_color(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)

        background = selenium.find_element_by_tag_name(
            'form').value_of_css_property('background-color')

        self.assertIn('rgba(0, 0, 0, 0)', background)

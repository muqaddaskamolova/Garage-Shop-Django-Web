from unittest import skip
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from garage.store.models import Category, Product
from django.http import HttpResponse, HttpRequest
from garage.store.views import all_products


@skip('demonstrating skipping')
class TestSkip(TestCase):

    def test_skip_example(self):
        pass

    def test_home_page(self):
        """ Tests that a GET request works and renders the correct
              template"""
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')


class TestViewResponses(TestCase):
    def setup(self):
        self.client = Client
        self.factory = RequestFactory
        User.objects.create(username='admin')
        Category.objects.create(name='sport', slug='sport')
        Product.objects.create(category_id=1, title='makleran', created_by_id=1, slug='makleran',
                               price=100, image='http://')

    def test_url_allowed_hosts(self):
        """ Test allowed hosts"""
        response = self.client.get('/', HTTP_HOST='nonexistent.com')
        self.assertEqual(response.status_code, 400)

        response = self.client.get('/', HTTP_HOST='mydomain.com')
        self.assertEqual(response.status_code, 200)

    def test_detail_url(self):
        """Test product response status"""
        response = self.client.get(reverse('store:product_detail', kwargs={'/makleran'}))
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        """Test category response status"""
        response = self.client.get(reverse('store:category_list', kwargs={'sport'}))
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        """ Tests that a GET request works and renders the correct
          template"""
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>ITALY GARAGE</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/sport')
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>ITALY GARAGE</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from garage.store.models import Category, Product
from django.utils import timezone


# from django.core import urlresolvers
# models test
class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Django', slug='Django')

    def test_category_creation(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(data.__unicode__(), data.name)


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Django', slug='Django')
        User.objects.create(username='admin')

        self.data1 = Product.objects.create(category_id=1, name='django_beginners', created_by_id=1,
                                            slug='django_beginners', price='20.00', image='django')

    def test_products_creation(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django_beginners')

    def test_products_url(self):
        data = self.data1
        url = reverse('store:product_detail', kwargs={'slug': data.slug})
        self.assertEqual(url, '/makleran')
        response = self.client.post(reverse('store:product_detail', kwargs={'slug': data.slug}))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """Test category custom manager basic"""
        data = Product.products.all()
        self.assertEqual(data.count(), 1)


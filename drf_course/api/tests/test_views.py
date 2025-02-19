from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from api.models import Product


class TestIndexPage(TestCase):
    
    # def test_index_page_status_code(self):
    #     """'assertContains' checks for status_code==200"""
    #     response = self.client.get(reverse('index'))
    #     self.assertEqual(response.status_code, 200)

    def test_index_page_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_contains_welcome_message(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Page created for testing purposes.')


class TestProductsPage(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000, stock=6)
        Product.objects.create(name="Phone", price=800, stock=8)

    def test_products_uses_correct_template(self):
        response = self.client.get(reverse('products-test'))
        self.assertTemplateUsed(response, 'products-test.html')

    def test_products_context(self):
        response = self.client.get(reverse('products-test'))
        self.assertEqual(len(response.context['products']), 2)
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Phone")
        self.assertNotContains(response, "No products available")

    def test_products_view_no_products(self):
        Product.objects.all().delete()
        response = self.client.get(reverse('products-test'))
        self.assertContains(response, "No products available")
        self.assertEqual(len(response.context['products']), 0)

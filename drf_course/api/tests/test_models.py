from django.core.exceptions import ValidationError
from django.test import TestCase

from api.models import Product


# python manage.py test
# python manage.py test api.tests.test_models
class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name="Test Product", price=100.00, stock=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        # Set stock count to 0 and test again
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discount_price(self):
        self.assertEqual(self.product.get_discounted_price(20), 80)
        self.assertEqual(self.product.get_discounted_price(40), 60)
        self.assertEqual(self.product.get_discounted_price(0), 100)

    def test_negative_price_validation(self):
        self.product.price = -10
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_count_validation(self):
        self.product.stock = -5
        with self.assertRaises(ValidationError):
            self.product.clean()

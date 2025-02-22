from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase

from api.models import Product


# python manage.py test
# python manage.py test api.tests.test_models
class ProductModelTest(TestCase):
    """The ProductModelTest class contains unit tests related to the Product model."""

    @classmethod
    def setUpTestData(cls):
        cls.product = Product(name="Test Product", price=100.00, stock=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        # Set stock count to 0 and test again
        self.product.stock = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discount_price(self):
        self.assertEqual(self.product.get_discounted_price(20), 80)
        self.assertEqual(self.product.get_discounted_price(40), 60)
        self.assertEqual(self.product.get_discounted_price(0), 100)

    # This validation is moved to the ProductForm
    # def test_negative_price_validation(self):
    #     self.product.price = -10
    #     with self.assertRaises(ValidationError):
    #         self.product.clean()

    # def test_negative_stock_count_validation(self):
    #     self.product.stock = -5
    #     with self.assertRaises(ValidationError):
    #         self.product.clean()

    def test_negative_price_constraint(self):
        """Test that a product with a negative price cannot be saved due to the database constraint."""
        product = Product(name="Negative Price Product", price=-1.00, stock=5)
        with self.assertRaises(IntegrityError):
            product.save()

    def test_zero_price_constraint(self):
        """Test that a product with a price of zero can be saved to the database."""
        product = Product(name="Zero Price Product", price=0, stock=5)
        product.save()

    def test_negative_stock_count_constraint(self):
        """Test that a product with a negative stock count cannot be saved due to the database constraint."""
        product = Product(name="Negative Stock Count Product", price=5, stock=-5)
        with self.assertRaises(IntegrityError):
            product.save()

    def test_zero_stock_count_constraint(self):
        """Test that a product with a stock count of zero can be saved to the database."""
        product = Product(name="Zero Stock Count Product", price=5, stock=0)
        product.save()

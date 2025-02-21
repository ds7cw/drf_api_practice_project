from django.test import TestCase
from django.urls import reverse

from api.models import Product


# python manage.py test
# python manage.py test api.tests.test_forms
class ProductFormTest(TestCase):
    def test_create_product_when_submitting_valid_form(self):
        """Test that form submission with valid data creates a product in the database."""
        form_data = {
            'name': 'Tablet',
            'price': 299.99,
            'stock': 50
        }
        response = self.client.post(reverse('products-test'), data=form_data)

        # Check that the product was created and we were redirected
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Tablet').exists())

    def test_dont_create_product_when_submitting_invalid_form(self):
        """Test that form submission with invalid data does not create a product."""
        form_data = {
            'name': '', # Name is required, validation error should be triggered
            'price': -50.00, # Negative price should trigger a validation error
            'stock': -5
        }
        response = self.client.post(reverse('products-test'), data=form_data)

        # Check that we get a 200 status (stay on the page to correct errors)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)

        form = response.context['form']
        self.assertFormError(form, 'name', 'This field is required')
        self.assertFormError(form, 'price', 'Price cannot be negative')
        self.assertFormError(form, 'stock', 'Stock count cannot be negative')
        self.assertFalse(Product.objects.exists())

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import Order, User


# python manage.py test
# python manage.py test api.tests.test_api
class UserOrderTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='test')
        self.user2 = User.objects.create_user(username='user2', password='test')
        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user1)
        Order.objects.create(user=self.user2)
        Order.objects.create(user=self.user2)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('order-list'))

        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(order['user'] == self.user2.id for order in orders['results']))

    def test_user_order_list_unauthenticated(self):
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


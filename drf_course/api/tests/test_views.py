from django.test import SimpleTestCase, TestCase
from django.urls import reverse


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

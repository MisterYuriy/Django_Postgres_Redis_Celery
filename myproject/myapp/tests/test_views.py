import json

from django.test import TestCase, Client
from django.urls import reverse

class UrlTagsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        client = Client()

    def test_main_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Ukr Energo Test Task')
       
    def test_calculate(self):
        data = json.dumps({"users_url": "https://google.com"})
        response = self.client.post("/myapp/calculate/", data,
                                    content_type='application/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data')
        
# Create your tests here.

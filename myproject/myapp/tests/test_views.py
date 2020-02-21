import json

from django.test import TestCase, Client
from django.urls import reverse


class UrlTagsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        client = Client()

    def test_main_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Круговая диаграмма')
       
    def test_calculate(self):
        data = json.dumps({"users_url": "https://google.com"})
        response = self.client.post("/myapp/calculate/", data,
                                    content_type='application/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data')
        
'''       
    def test_url_max_length(self):
        urltags = UrlTags.objects.get(id=1)
        max_length = urltags._meta.get_field('url').max_length
        self.assertEquals(max_length, 400)

    def test_datetime_autonow(self):
        urltags = UrlTags.objects.get(id=1)
        auto_now = urltags._meta.get_field('datetime').auto_now
        self.assertTrue(auto_now)
    
    def test_json_field(self):
        urltags = UrlTags.objects.get(id=1)
        json_type = urltags._meta.get_field('params').db_type('connection')
        self.assertTrue(json_type, 'jsonb')

    def test_object_name_is_last_name_comma_first_name(self):
        urltags = UrlTags.objects.get(id=1)
        expected_object_name = '{0}, {1}'.format(urltags.url, urltags.datetime)
        self.assertEquals(expected_object_name,str(urltags))
'''
# Create your tests here.

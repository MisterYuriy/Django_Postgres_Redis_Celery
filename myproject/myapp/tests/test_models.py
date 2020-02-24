from django.test import TestCase

from myapp.models import UrlTags

class UrlTagsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UrlTags.objects.create(url='https://www.google.com/', params='uih')

    def test_url_label(self):
        urltags = UrlTags.objects.get(id=1)
        field_label = urltags._meta.get_field('url').verbose_name
        self.assertEquals(field_label,'url')
       
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
        
# Create your tests here.

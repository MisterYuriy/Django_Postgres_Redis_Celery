from django.db import models
from django.contrib.postgres.fields import JSONField

class UrlTags(models.Model):

    url = models.URLField(max_length=400)
    datetime = models.DateTimeField(auto_now=True)
    params = JSONField()
    
    def __str__(self):
        return '{0}, {1}'.format(self.url, self.datetime)

# Create your models here.

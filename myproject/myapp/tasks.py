from __future__ import absolute_import, unicode_literals

import requests

from celery import shared_task, task
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from html.parser import HTMLParser

from .models import UrlTags

def validate_url(url):
    val = URLValidator()
    try:
        val(url)
        content = requests.get(url).content
        return content
    except:
        return False

@task
def calculate_task(url):
    # validate url
    content = validate_url(url)
    if not content:
        return {'message': 'Url is not valid or not available', 'status': 400}
    
    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):
        tags = {}
        def handle_starttag(self, tag, attrs):
            if tag not in self.tags:
                self.tags[tag] = 1
            else:
                self.tags[tag] += 1

    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(content.decode("utf-8"))
    
    # create data list
    data = [[k,v] for k,v in parser.tags.items()]
    data.insert(0, ['Tags', 'Count_Tags'])
    
    # create and save model
    urltags = UrlTags(url=url, params=data)
    urltags.save()
    return {'data': data, 'status': 200}


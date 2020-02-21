import json

from django.shortcuts import render
from django.http import Http404, JsonResponse

from .tasks import calculate_task

def home(request):
    return render(request, 'main.html')
    
def calculate(request):
    if request.is_ajax() and request.method == 'POST':
        url = json.loads(request.body).get('users_url')
        task = calculate_task.delay(url)
        return JsonResponse(task.get())
    else:
        raise Http404
    
    
# Create your views here.

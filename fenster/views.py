from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('fenster/index.html')
    context = {
        "window_height": 100,
        "window_width": 50,
    }
    return HttpResponse(template.render())

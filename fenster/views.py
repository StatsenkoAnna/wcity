from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Fenster
from random import randint

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    #test_creation()
    context = {
        "request_place": str(request)
    }
    try:
        if 'selected_fenster' in request.POST:
            fenster_id = request.POST('selected_fenster')
            return buy(request, fenster_id)
        context['request_place'] += str(request.POST)
    except Exception as e:
        context["an exception"] = str(e) + str(type(e))
    return display_all(request, context)

def buy(request, fenster_id):
    all_fensters = Fenster.objects
    Fenster.objects.filter(id=fenster_id).delete()
    return display_all(request)

def display_all(request, context={}):
    fenster_list = Fenster.objects.order_by('id')
    context["fenster_list"] = fenster_list
    return render(request, 'fenster/index.html', context)

@login_required
def sell(request):
#Sell a fenster.
    if request.method == "GET":
        return render(request, 'fenster/new.html')
    elif request.method == "POST":
        f = Fenster(
        fenster_width=request.POST["fenster_width"],
        fenster_height=request.POST["fenster_height"],
        fenster_scheme=request.POST["fenster_scheme"],
        window_view='')
    f.save()

def test_creation():
#Create a new fenster.
    f = Fenster(
        fenster_width=randint(100,256),
        window_view=''
    )
    f.save()

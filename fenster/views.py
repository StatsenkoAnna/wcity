from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Fenster
from random import randint
from django.core.mail import send_mail
from .pss import yapass
import logging
import os


logger = logging.getLogger(__name__)

def index(request):
    #test_creation()
    context = {
        "request_place": str(request)
    }
    try:
        print(str(request.POST))
        if 'selected_fenster' in request.POST:
            fenster_id = request.POST['selected_fenster']
            return buy(request)
        context['request_place'] += str(request.POST)
    except Exception as e:
        context["an exception"] = str(e) + str(type(e))
    return display_all(request, context)

def buy(request):
    if request.method == 'POST':
        print(str(request.POST))
        if 'selected_fenster' in request.POST:
            f = Fenster.objects.get(pk=request.POST['selected_fenster'])
            f.save()
            print("\n\nSOOOOOLD!%s\n\n" % request.POST['selected_fenster'])
            logger.log(
                'Fenster #%i was sold.' % (
                     request.POST['selected_fenster']
            ))
            print('kuku')
            os.sys.stdout.flush()
            send_mail(
                subject='Fenster was sold',
                message='Fenster #%i was sold.' % f.id,
                from_email='anna26071145@yandex.ru',
                recipient_list=['anna190711@gmail.com'],
                auth_user="anna26071145",
                auth_password=yapass,
                fail_silently=False
                )
    return HttpResponseRedirect("/fenster")

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

from django.shortcuts import render,HttpResponse
from blog import signals

# Create your views here.
def home(request):
    signals.notification.send(request=request,sender=None,user=['geeky','shows'])
    return HttpResponse('You get notificated by Custom signal')
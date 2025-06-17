from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def main(request):
    print('This is view call')
    return HttpResponse('I am Class Based View')

def excp(request):
    print('This is exception from view')
    a = 255/0
    return HttpResponse(a)

def user(request):
    print('user info from view')
    context = {
        'name': 'Rahul'
    }
    return TemplateResponse(request, 'main/user.html', context)
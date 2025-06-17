from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

def home(request):
    cache.set('movie','The one',30)
    mv = cache.get('movie')
    print(mv)
    return render(request,'enroll/home.html',{'mv':mv})

def home2(request):
    mv = cache.get_or_set('teacher',20, 30)
    return render(request,'enroll/home.html',{'mv':mv})


def home3(request):
    cache.clear()
    x = cache.get('teacher', 'NoTeacher')
    y = cache.get('movie', 'NoMovie')
    print('Cache Cleared!!')
    return render(request,'enroll/home.html',{'x':x, 'y':y})
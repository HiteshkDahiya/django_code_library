from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.


# @cache_page(timeout=60)              #---> one way to do The Per-view Cache --->second one is to apply it to url
def home(request):
    return render(request,'home/home.html')


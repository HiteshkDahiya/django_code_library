from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def try1(request):
    return render(request,'main/try1.html')

def try2(request):
    return render(request,'main/try2.html')
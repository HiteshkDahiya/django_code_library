from django.shortcuts import render

# Create your views here.
def try0(request):
    return render(request,'main/index.html')

def try1(request):
    return render(request,'try/try1.html')


def try2(request):
    return render(request,'try/try2.html')

def try3(request):
    return render(request,'try/try3.html')

def try4(request):
    return render(request,'try/try4.html')
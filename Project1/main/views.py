from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def about(request):
    return render(request,'main/about.html')

def index(request):
    return render(request,'main/index.html')



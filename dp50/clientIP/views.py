from django.shortcuts import render

# Create your views here.
def home(request):
    ip = request.session.get('ip',0)
    return render(request,'clientIP/home.html',{'ip':ip})
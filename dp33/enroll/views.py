from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if 'login' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.error(request,'Username not found!!')
            elif 'signup' in request.POST:
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username is already exist!')
                else:
                    user = User.objects.create_user(username,email,password)
                    user.save()
                    messages.success(request,"User created!!")
                    return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/profile/')

    return render(request,'enroll/auth.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html')
    else:
        return HttpResponseRedirect('/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
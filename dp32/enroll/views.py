from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm
# Create your views here.

def log_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            if 'login' in request.POST:
                fm = AuthenticationForm(request=request,data=request.POST)
                if fm.is_valid():
                    nm = fm.cleaned_data['username']
                    ps = fm.cleaned_data['password']
                    user = authenticate(request,username=nm,password=ps)
                    if user:
                        login(request, user)
                        return HttpResponseRedirect('/profile/')
                    else:
                        return HttpResponseRedirect('/signup/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/log_in.html',{'form':fm})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            messages.success(request,'forms save successfully!!')
            fm.save()
    else:
        fm = UserForm()
    return render(request,'enroll/sign_up.html',{'form':fm})

def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html')
    else:
        return HttpResponseRedirect('/')

def not_found(request):
    return render(request,'enroll/notfound.html')
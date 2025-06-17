from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import Sign_up
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = Sign_up(request.POST)
        if fm.is_valid():
            messages.success(request, "Form Submitted Successfully!!")
            messages.info(request, "add another user")
            fm.save()
    else:
        fm = Sign_up()
    return render(request, 'enroll/sign_up.html', {'form': fm})


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/log_in.html', {'form': fm, })
    else:
        return HttpResponseRedirect('/profile/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def edit_profile(request):
    user = request.user
    if request.method == "POST":
        fm = Sign_up(request.POST, instance=user)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            last_name = fm.cleaned_data['last_name']
            print(username)
            print(last_name)
            fm.save()
            messages.success(request,'user Info updated successfully!!')
            return HttpResponseRedirect('/profile/')
        else:
            print(fm.errors.as_data())
    else:
        fm = Sign_up(instance=user)

    return render(request, 'enroll/edit_profile.html', {'form': fm})
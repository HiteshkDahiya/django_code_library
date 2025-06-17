from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserProfileForm, UserEditProfileForm


# Create your views here.
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request,'You logged in Successfully !')
                    return redirect('/userprofile/')

                else:
                    messages.success(request,'Username not found!!')
                    return redirect('/signin/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/log_in.html',{'form':fm})
    else:
        return redirect('/profile/')

def log_out(request):
    logout(request)
    return redirect('/')

def sign_in(request):
    if request.method == 'POST':
        fm = UserProfileForm(request.POST)
        if fm.is_valid():
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exist.')
                return redirect('/signin/')
            else:
                fm.save()
                messages.success(request, 'You signIn in Successfully !')
                return redirect('/')
    else:
        fm = UserProfileForm()
    return render(request,'enroll/sign_in.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserEditProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated Successfully !!')
                fm.save()

        else:
            fm = UserEditProfileForm(instance=request.user)
        return render(request, 'enroll/profile.html',{'form':fm})
    else:
        return redirect('/')

def change_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'enroll/changePass.html',{'form':fm})
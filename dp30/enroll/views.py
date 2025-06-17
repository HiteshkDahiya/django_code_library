from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        if "login" in request.POST:  # Login logic
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("/profile/")  # Redirect to home page
            else:
                messages.error(request, "Invalid username or password.")

        elif "signup" in request.POST:  # Signup logic
            username = request.POST["new_username"]
            email = request.POST["email"]
            password = request.POST["new_password"]
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.success(request, "Account created! You can log in now.")
                return redirect("/")  # Reload same page

    return render(request, "enroll/auth.html")

def profile(request):
    if request.user is not authenticate:
        return redirect("/")
    else:
        return render(request,'enroll/profile.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
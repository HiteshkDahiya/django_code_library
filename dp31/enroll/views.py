from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Form saved successfully!')
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')

    else:
        fm = UserCreationForm()
    return render(request,'enroll/home.html',{'form':fm})
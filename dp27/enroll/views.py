from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Form Submitted Successfully!!")
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'enroll/sign_up.html',{'form':fm})
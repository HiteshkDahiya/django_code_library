from django.shortcuts import render
from django.contrib import messages
from .forms import Sign_up


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = Sign_up(request.POST)
        if fm.is_valid():
            messages.success(request,"Form Submitted Successfully!!")
            messages.info(request,"add another user")
            fm.save()
    else:
        fm = Sign_up()
    return render(request, 'enroll/sign_up.html',{'form':fm})
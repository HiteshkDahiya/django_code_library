from django.shortcuts import render

# Create your views here.
def enroll(request):
    return render(request,'enroll/enroll.html')

def signup(request):
    return render(request,'enroll/signup.html')
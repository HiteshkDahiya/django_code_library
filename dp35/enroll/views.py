from django.shortcuts import render

# Create your views here.
def enroll(request):
    show_modal = True
    return render(request,'enroll/enroll.html',{'show_modal':show_modal})
from django.shortcuts import render
from .models import ExamCenter,MyExamCenter

# Create your views here.
def home(request):
    mdata = MyExamCenter.objects.all()
    return render(request,'school/home.html',{'mdata':mdata})
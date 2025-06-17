from django.shortcuts import render
from school.models import Student, StudentProxy


# Create your views here.
def home(request):
    student_data = StudentProxy.objects.all()
    # student_data = StudentProxy.students.order_by()
    return render(request,'school/home.html',{'students':student_data})
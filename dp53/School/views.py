from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):

    Sdata = Student.objects.all()
    Tdata = Teacher.objects.all()

    # data = Student.objects.filter(id = 4)

    # Sdata = Student.objects.order_by('name')
    # Sdata = Student.objects.order_by('-name')
    # Sdata = Student.objects.order_by('?')

    # Sdata = Student.objects.order_by('-name').reverse()

    # data = Student.objects.values_list('id','name',named=True)

    # data = Student.objects.using('default').all()

    data = Student.objects.none()

    # qs1 = Student.objects.values('id','name')
    # qs2 = Teacher.objects.values('id','name')
    # data = qs1.union(qs2,all=True)

    # qs1 = Student.objects.values('id', 'name')
    # qs2 = Teacher.objects.values('id', 'name')
    # data = qs1.intersection(qs2)

    # qs1 = Student.objects.values('id', 'name')
    # qs2 = Teacher.objects.values('id', 'name')
    # data = qs1.difference(qs2)

    # data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)

    # data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)


    # data = Student.objects.filter(Q(id=6) | Q(roll=109))
    print(data)
    return render(request,'school/home.html',{'data':data, 'Sdata':Sdata, 'Tdata':Tdata})
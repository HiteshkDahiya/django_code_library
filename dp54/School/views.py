from importlib.metadata import pass_none

from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):
    Sdata = Student.objects.all()
    Tdata = Teacher.objects.all()
    data = Student.objects.get(pk=1)

    # data = Student.objects.first()

    # data = Student.objects.last()

    # data = Student.objects.earliest('passed_date')

    # data = Student.objects.latest('passed_date')

    # data = Student.objects.create(name='hameez', roll=111, city='jamnagar', marks= 89, passed_date='2025-4-11')

    # data,created = Student.objects.get_or_create(name='nawazuddin', roll=111, city='jamnagar', marks= 89, passed_date='2025-4-11')

    # data = Student.objects.filter(id=12).update(name='nawazuddin', roll=112)

    # data,created = Student.objects.update_or_create(id=13, defaults={'name':'sareena','roll':113})

    # objs = [
    #     Student(name='sareef',roll=115,city='barmer',marks=80,passed_date='2024-4-11'),
    #     Student(name='sareef',roll=116,city='barmer',marks=80,passed_date='2024-4-11'),
    #     Student(name='sareef',roll=117,city='barmer',marks=80,passed_date='2024-4-11'),
    #     Student(name='sareef',roll=118,city='barmer',marks=80,passed_date='2024-4-11'),
    # ]
    # data = Student.objects.bulk_create(objs)

    # data = Student.objects.all()
    # for dt in data:
    #     dt.city = 'ahmdabad'
    # student_data = Student.objects.bulk_update(data,['city'])

    # data = Student.objects.in_bulk([1,4])
    # print(data[1].city)



    # data = Student.objects.in_bulk([])
    # data = Student.objects.in_bulk()
    # print(data[1].name)

    # data = Student.objects.filter(id=18).delete()
    # data = Student.objects.filter(marks=80).delete()

    # data = Student.objects.update_or_create(id=1,defaults={'city':'ahmdabaad'})

    # data = Student.objects.filter(marks=88).count()
    print(data)
    # print(created)
    return render(request,'school/home.html',{'student':data, 'Sdata':Sdata, 'Tdata':Tdata})
from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.

def home(request):
    Sdata = Student.objects.all()

    # data = Student.objects.filter(passdate__range=('2025-04-02','2025-04-12'))

    data = Student.objects.filter(admdatetime__date=date(2025,2,14))

    data = Student.objects.filter(passdate=date(2025,4,10))


    # data = Student.objects.filter(passdate__year= 2024)


    # data = Student.objects.filter(passdate__month= 4)


    # data = Student.objects.filter(passdate__day= 5)


    # data = Student.objects.filter(passdate__week= 15)


    # data = Student.objects.filter(passdate__week_day= 5)


    # data = Student.objects.filter(passdate__quarter= 2)


    # data = Student.objects.filter(admdatetime__time__gt= time(6,00))


    # data = Student.objects.filter(admdatetime__hour__gt= 5)

    # data = Student.objects.filter(admdatetime__minute__gt= 23)

    # data = Student.objects.filter(admdatetime__second__gt= 23)

    print('Return:', data)
    print()
    print("SQL Query:",data.query)
    return render(request,'school/home.html',{'students':data,'Sdata':Sdata})


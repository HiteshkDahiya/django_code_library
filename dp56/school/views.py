from django.shortcuts import render
from .models import Student
from django.db.models import Avg,Sum,Min,Max,Count
# Create your views here.

def home(request):
    data = Student.objects.all()

    average = Student.objects.aggregate(Avg('marks'))
    total = Student.objects.aggregate(Sum('marks'))
    minimum = Student.objects.aggregate(Min('marks'))
    maximum = Student.objects.aggregate(Max('marks'))
    count = Student.objects.aggregate(Count('marks'))

    context = {
        'students': data,'average':average,'minimum':minimum,'maximum':maximum, 'count':count, 'total':total
    }
    print('Return:', data)
    print()
    print("SQL Query:",data.query)
    return render(request,'school/home.html',context)


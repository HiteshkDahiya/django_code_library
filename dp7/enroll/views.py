from django.template import loader
from django.http import HttpResponse
from .models import Student

def studetails(request):
    stu = Student.objects.all()
    template = loader.get_template('enroll/enroll.html')
    context = {
        'stu' : stu
    }
    return HttpResponse(template.render(context,request))

def getdetails(request,id):
    stu1 = Student.objects.get(id=id)
    template = loader.get_template('enroll/enroll1.html')
    context = {
        'stu1' : stu1
    }
    return HttpResponse(template.render(context,request))
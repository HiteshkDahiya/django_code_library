from django.template import loader
from django.http import HttpResponse
from .models import Student

def students(request):
    template = loader.get_template('enroll/enroll.html')
    stu = Student.objects.all()
    context = {
        'stu' : stu
    }
    return HttpResponse(template.render(context,request))
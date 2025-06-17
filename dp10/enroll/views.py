from django.template import loader
from .forms import StudentRegistration
from django.http import HttpResponse

# Create your views here.
def students(request):
    template = loader.get_template("enroll/enroll.html")
    fm = StudentRegistration()
    context = {
        "form" : fm
    }
    return HttpResponse(template.render(context, request))
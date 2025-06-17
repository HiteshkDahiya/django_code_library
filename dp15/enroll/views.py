from django.template import loader
from .forms import St
from django.http import HttpResponse

# Create your views here.
def st(request):
    template = loader.get_template("enroll/enroll.html")
    form = St()
    context = {
        "form" : form
    }
    return HttpResponse(template.render(context, request))
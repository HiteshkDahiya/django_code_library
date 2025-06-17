from django.template import loader
from .forms import StudentRegistration
from django.http import HttpResponse

# Create your views here.
def students(request):
    template = loader.get_template("enroll/enroll.html")
    form = StudentRegistration(auto_id="some_%s", label_suffix='--', initial={} )
    form.order_fields(field_order = ['name','email','first_name',])
    context = {
        "form" : form
    }
    return HttpResponse(template.render(context, request))


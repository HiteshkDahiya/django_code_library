from django.http import HttpResponse
from django.template import loader

# Create your views here.
def convert(request,year):
    template = loader.get_template('enroll/enroll.html')
    context = {
        'yr': year
    }
    return HttpResponse(template.render(context,request))
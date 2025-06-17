from re import template

from django.template import loader
from .forms import St
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here
def showdata(request):
    template = loader.get_template("enroll/enroll.html")
    if request.method == 'POST':
        fm = St(request.POST)
        if fm.is_valid():
          print('data validated')
          print("Name:",fm.cleaned_data['name'])
          print("Roll:", fm.cleaned_data['roll'])
          print("Dec No.:", fm.cleaned_data['dnum'])
          print("Float No.:", fm.cleaned_data['fnum'])
          print("URL:", fm.cleaned_data['url'])
          print("Feedback:", fm.cleaned_data['feedback'])
          print("Description:", fm.cleaned_data['description'])
          print("Agree:",fm.cleaned_data['agree'])
          return HttpResponseRedirect('/')
    else:
        fm = St()
    context = {
        "form" : fm
    }
    return HttpResponse(template.render(context, request))
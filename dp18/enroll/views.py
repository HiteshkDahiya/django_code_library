from django.template import loader
from .forms import St
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here
def response(request):
    template = loader.get_template('enroll/response.html')
    return HttpResponse(template.render())

def showdata(request):
    template = loader.get_template("enroll/enroll.html")
    if request.method == 'POST':
        fm = St(request.POST)
        if fm.is_valid():
          print('data validated')
          print("Name:",fm.cleaned_data['name'])
          print("Email",fm.cleaned_data['email'])
          print("Password:",fm.cleaned_data['password'])
          return HttpResponseRedirect('/success')
    else:
        fm = St()
    context = {
        "form" : fm
    }
    return HttpResponse(template.render(context, request))
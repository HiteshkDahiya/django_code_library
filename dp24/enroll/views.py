from django.template import loader
from .forms import St
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data


# Create your views here
def showdata(request):
    template = loader.get_template("enroll/enroll.html")
    if request.method == 'POST':
        fm = St(request.POST)
        if fm.is_valid():
          print('data validated')
          nm = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          ps = fm.cleaned_data['password']
          #will add
          user = Data(name=nm,email=em,password=ps)
          user.save()
          #will update
          # user = Data(id=2,name=nm,email=em,password=ps)
          # user.save()
          #will delete
          # user = Data(id=2)
          # user.delete()
          return HttpResponseRedirect('/')
    else:
        fm = St()
    context = {
        "form" : fm
    }
    return HttpResponse(template.render(context, request))
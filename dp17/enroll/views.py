from django.template import loader
from .forms import StudentForm
from django.http import HttpResponse

# Create your views here.
def save_data(request):
    template = loader.get_template("enroll/enroll.html")
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
          print('data validated')
          print("Name:",fm.cleaned_data['name'])
          print("Email",fm.cleaned_data['email'])
          print("Password:",fm.cleaned_data['password'])
    else:
        fm = StudentForm()
    context = {
        "form" : fm
    }
    return HttpResponse(template.render(context, request))
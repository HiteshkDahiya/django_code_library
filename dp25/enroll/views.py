from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Student
from .models import DataA,DataB

# Create your views here
def classs(request,check):
    template = loader.get_template('enroll/home.html')
    context = {
        'ch':check
    }
    return HttpResponse(template.render(context,request))

def students(request,check):
    template = loader.get_template('enroll/students.html')
    stuA = DataA.objects.all()
    stuB = DataB.objects.all()
    context = {
        'ch':check,
        'stuA':stuA,
        'stuB':stuB
    }
    return HttpResponse(template.render(context,request))

def details_a(request,check,id):
    template = loader.get_template('enroll/details.html')
    stu = DataA.objects.get(id = id)
    context = {
        'ch':check,
        'stu':stu,
        "id":id
    }
    return HttpResponse(template.render(context,request))

def details_b(request,check,id):
    template = loader.get_template('enroll/details.html')
    stu = DataB.objects.get(id = id)
    context = {
        'ch':check,
        'stu':stu,
        "id":id
    }
    return HttpResponse(template.render(context,request))

def registration(request,check):
    template = loader.get_template('enroll/registration.html')
    context = {
        'ch':check
    }
    return HttpResponse(template.render(context,request))

def registration_in_a(request,check):
    template = loader.get_template('enroll/enrollA.html')
    if request.method == 'POST':
        st = Student(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['name']
            em = st.cleaned_data['email']
            ps = st.cleaned_data['password']
            user = DataA(name=nm,email=em,password=ps)
            user.save()
            return HttpResponseRedirect('/')
    else:
        st = Student()
    context = {
        "formA" : st,
        'ch' : check
    }
    return HttpResponse(template.render(context,request))

def registration_in_b(request,check):
    template = loader.get_template('enroll/enrollB.html')
    if request.method == 'POST':
        st = Student(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['name']
            em = st.cleaned_data['email']
            ps = st.cleaned_data['password']
            user = DataB(name=nm,email=em,password=ps)
            user.save()
            return HttpResponseRedirect('/')
    else:
        st = Student()
    context = {
            "formB" : st,
            'ch' : check
    }
    return HttpResponse(template.render(context,request))
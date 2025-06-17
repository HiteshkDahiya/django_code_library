from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import StudentForm
from .models import StudentRegistration
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# This is Show And Add View
class HomeTemplateView(TemplateView):
    template_name = 'enroll/enroll.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stu = StudentForm()
        data = StudentRegistration.objects.all()
        context = {
            'stu': stu,
            'data': data
        }
        return context

    def post(self,request):
        stu = StudentForm(request.POST)
        if stu.is_valid():
            nm = stu.cleaned_data['name']
            em = stu.cleaned_data['email']
            ps = stu.cleaned_data['password']
            user = StudentRegistration(name = nm, email = em, password = ps)
            user.save()
            return HttpResponseRedirect('/')

#This is Delete View
class DeleteRedirectView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        id = kwargs['id']
        StudentRegistration.objects.get(id=id).delete()
        return super().get_redirect_url(*args,**kwargs)

#This is Update View
class UpdateView(View):
    def get(self,request,id):
        pi = StudentRegistration.objects.get(id=id)
        stu = StudentForm(instance=pi)
        return render(request, 'enroll/update.html', {'stu': stu, 'pi': pi})

    def post(self,request,id):
        pi = StudentRegistration.objects.get(id=id)
        stu = StudentForm(request.POST, instance=pi)
        if stu.is_valid():
            stu.save()
            return HttpResponseRedirect('/')


from django.shortcuts import HttpResponse,render
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
##################################################################################
def func(request):
    return HttpResponse('<h1>This is function based view</h1>')

class Class(View):
    name = 'sonam'
    def get(self,request):
        # return HttpResponse('<h1>This is Class based view - GET</h1>')
        return HttpResponse(self.name)

class ClassChild(Class):
    def get(self,request):
        return HttpResponse(self.name)


################################################################################
def func2(request):
    context = {
        'msg' : 'This is function based views. using render and context.'
    }
    return render(request,'myapp/home.html',context)

class Cls2(View):
    def get(self,request):
        context = {'msg': "This is Class Based view. Using render and context."}
        return render(request,'myapp/home.html',context)

##################################################################################
def func3(request):
    my_template = 'myapp/home.html'
    context = {
        'msg' : 'This is function based views. Function3.'
    }
    return render(request,my_template,context)

class Cls3(View):
    my_template = 'myapp/home.html'
    def get(self,request):
        context = {'msg': "This is Class Based view. Class3."}
        return render(request,self.my_template,context)

##################################################################################
def func4(request,temp):
    my_template = temp
    context = {
        'msg' : 'This is function based views. Function4.'
    }
    return render(request,my_template,context)

class Cls4(View):
    temp = ''
    def get(self,request):
        context = {'msg': "This is Class Based view. Class4."}
        return render(request,self.temp,context)
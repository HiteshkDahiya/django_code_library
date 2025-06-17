from django.shortcuts import render,HttpResponse

# Create your views here.
def main(request):
    print('I am view')
    return HttpResponse('i am view')
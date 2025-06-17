from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    response = render(request, 'cookie/set_cookie.html')
    response.set_cookie('name','shilpa')
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'cookie/get_cookie.html',{'name':name})


def delete_cookie(request):
    response = render(request, 'cookie/del_cookie.html')
    response.delete_cookie('name')
    return response
from django.shortcuts import render
from .models import Page,Post,Song

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')


def page(request):
    data = Page.objects.all()
    data = Page.objects.filter(page_name='geekyshows')
    # data = Page.objects.filter(user__first_name='sonam')
    context = {
        'data':data,
    }
    return render(request,'myapp/page.html',context)


def post(request):
    data = Post.objects.all()
    context = {
        'data':data,
    }
    return render(request,'myapp/post.html',context)


def song(request):
    data = Song.objects.all()
    context = {
        'data':data,
    }
    return render(request,'myapp/song.html',context)
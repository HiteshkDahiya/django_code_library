from django.core.cache import cache
from django.shortcuts import render,redirect
from .forms import SignUpForm,LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import User,Group

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'home/home.html',{'posts':posts})

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
            messages.success(request,"You have signup to new account!!")
            return redirect('/signup/')
    else:
        fm = SignUpForm()
    return render(request,'home/signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LogInForm(request=request,data=request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'you have login successfully!!')
                return redirect('/dashboard/')
            else:
                messages.error(request,'Wrong Password or Input!!')
        else:
            fm = LogInForm(request=request)
        return render(request,'home/login.html',{'form':fm})
    else:
        return redirect('/dashboard/')

def user_logout(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        ct = cache.get('count',version=user.pk)
        return render(request,'home/dashboard.html',{'posts':posts,'ct':ct})
    else:
        return redirect('/login/')

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        disc = request.POST['disc']
        post = Post.objects.create(title=title,disc=disc)
        post.save()
        return redirect('/addpost/')

    return render(request, 'home/add_post.html')

def edit_post(request,id):
    post = Post.objects.get(id= id)
    if request.method == 'POST':
        title = request.POST['title']
        disc = request.POST['disc']
        post.title = title
        post.disc = disc
        post.save()
        return redirect('/dashboard/')

    return render(request, 'home/edit_post.html',{'post':post})

def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/dashboard/')

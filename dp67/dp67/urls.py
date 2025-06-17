"""
URL configuration for dp67 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('func/', views.func),
    path('cls/', views.Class.as_view(name='Rahul')),
    path('clsc/', views.ClassChild.as_view()),
    path('func2/', views.func2),
    path('cls2/', views.Cls2.as_view()),
    path('func3/', views.func3),
    path('cls3/', views.Cls3.as_view()),
    path('func4/', views.func4,{'temp':"myapp/home.html"}),
    path('cls4/', views.Cls4.as_view(temp='myapp/home.html')),
]

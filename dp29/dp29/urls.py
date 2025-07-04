"""
URL configuration for dp29 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign_up,name='signup'),
    path('login/', views.log_in,name='login'),
    path('logout/', views.log_out,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('edit_profile/', views.edit_profile,name='edit_profile'),
]


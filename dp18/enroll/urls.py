from django.urls import path
from . import views

urlpatterns = [
    path('',views.showdata,name='students'),
    path('success/',views.response,name='response')
]
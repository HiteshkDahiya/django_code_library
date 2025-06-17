from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('try1/', views.try1, name='try1'),
    path('try2/', views.try2, name='try2'),
]
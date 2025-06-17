from django.urls import path
from . import views

urlpatterns = [
    path('try0/',views.try0,name='try0'),
    path('try1/',views.try1,name='try1'),
    path('try2/',views.try2,name='try2'),
    path('try3/',views.try3,name='try3'),
    path('try4/',views.try4,name='try4'),
]
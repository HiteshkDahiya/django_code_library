from django.urls import path
from . import views

urlpatterns = [
    path('',views.enroll,name='enroll'),
    path('signup/',views.signup,name='signup')
]
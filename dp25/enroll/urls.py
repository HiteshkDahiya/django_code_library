from django.urls import path
from . import views

urlpatterns = [
    path('',views.classs,{'check':10},name='classs'),
    path('registration/',views.registration,{'check':10},name='registration'),
    path('details_a/<int:id>/',views.details_a,{'check':10},name='details_a'),
    path('details_b/<int:id>/',views.details_b,{'check':10},name='details_b'),
    path('students/',views.students,{'check':10},name='students'),
    path('enrollA/',views.registration_in_a,{'check':10},name='registrationa'),
    path('enrollB/',views.registration_in_b,{'check':10},name='registrationb')
]
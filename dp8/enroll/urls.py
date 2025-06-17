from django.urls import path
from . import views

urlpatterns = [
    path('',views.studetails,name='studetails'),
    path('details/<int:id>',views.getdetails,name='getdetails')
]
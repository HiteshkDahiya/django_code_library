from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_image,name='addimage'),
    path('show/', views.show_image,name='showimage')
]
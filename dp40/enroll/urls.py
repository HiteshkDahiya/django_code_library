from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('signin/',views.sign_in,name='signin'),
    path('userprofile/',views.user_profile,name='userprofile'),
    path('changepass/',views.change_pass,name='changepass'),
    path('get_details/<int:id>/',views.get_details,name='get_details'),
]
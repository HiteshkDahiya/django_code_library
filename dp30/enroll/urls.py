from django.urls import path
from .views import user_login
from .views import profile
from .views import log_out

urlpatterns = [
    path('', user_login, name='auth'),  # One page for both
    path('profile/', profile, name='profile'),
    path('logout/', log_out, name='logout'),
]
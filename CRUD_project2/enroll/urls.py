from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='home'),
    path('delete/<int:id>/',views.DeleteRedirectView.as_view(),name='deletedata'),
    path('update/<int:id>/',views.UpdateView.as_view(),name='updatedata'),
]
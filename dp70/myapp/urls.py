from django.urls import path
from myapp import views

urlpatterns = [
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
]

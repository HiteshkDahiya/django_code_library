from django.urls import path,register_converter
from . import views,converters

register_converter(converters.Year,'YYYY')

urlpatterns = [
    path('years/<YYYY:year>/',views.convert)
]
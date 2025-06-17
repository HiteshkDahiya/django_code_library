from django.contrib import admin
from .models import MyExamCenter


# Register your models here.
@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']
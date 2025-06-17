from django.contrib import admin
from .models import DataA,DataB


# Register your models here.
@admin.register(DataA)
class UserAdminA(admin.ModelAdmin):
    list_display = ('id','name','email','password')


@admin.register(DataB)
class UserAdminB(admin.ModelAdmin):
    list_display = ('id','name','email','password')


from django.contrib import admin
from.models import MyExamCenter,ExamCenter

# Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = (['id','cname','city'])


@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']
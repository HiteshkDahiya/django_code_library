from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stuid','stuname','stuemail','stupass']
    list_filter = ['stuname', 'stuid']
    search_fields = ('stuname', 'stuid')
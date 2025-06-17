from django.contrib import admin
from .models import Student

class SchoolStudent(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')

admin.site.register(Student, SchoolStudent)

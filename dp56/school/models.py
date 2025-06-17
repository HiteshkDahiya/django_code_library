from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=80)
    roll=models.IntegerField(unique=True)
    city=models.CharField(max_length=90)
    marks=models.IntegerField()
    passdate=models.DateField()
    admdatetime=models.DateTimeField()

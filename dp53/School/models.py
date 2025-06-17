from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=80)
    marks = models.IntegerField()
    passed_date = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    pass_key = models.IntegerField(unique=True)
    city = models.CharField(max_length=80)
    salary = models.IntegerField()
    joined_date = models.DateField()
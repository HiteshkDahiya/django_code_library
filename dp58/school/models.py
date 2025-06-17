from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=90)
    city = models.CharField(max_length=90)


class MyExamCenter(ExamCenter):
    name = models.CharField(max_length=90)
    roll = models.CharField(max_length=90)
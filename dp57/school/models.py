from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    cname = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    class Meta:
        abstract = True


class MyExamCenter(ExamCenter):
    name = models.CharField(max_length=80)
    roll = models.IntegerField()
from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname=models.CharField(max_length=80)
    city=models.CharField(max_length=80)



class MyExamCenter(ExamCenter):
    class Meta:
        proxy=True
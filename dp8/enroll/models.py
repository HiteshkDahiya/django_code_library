from django.db import models

class Student(models.Model):
    stuid = models.IntegerField(max_length=70)
    stuname = models.CharField(max_length=70)
    stuemail = models.CharField(max_length=70)
    stupass = models.CharField(max_length=70)

    def __str__(self):
        return self.stuname
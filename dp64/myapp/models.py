from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL,CASCADE


# Create your models here.
class Page(models.Model):
    # user = models.ForeignKey(User, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=SET_NULL,null=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    rel_date = models.DateField()
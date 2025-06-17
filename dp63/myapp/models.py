from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE,PROTECT

# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    # user = models.OneToOneField(User,on_delete=PROTECT)
    # user = models.OneToOneField(User,on_delete=PROTECT,limit_choices_to={'is_staff':True},primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_date = models.DateField()

class Like(Page):
    page = models.OneToOneField(Page, on_delete=CASCADE,parent_link=True)
    like_count = models.IntegerField()

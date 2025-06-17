from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    page_name = models.CharField(max_length=70)
    rel_date = models.DateField()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    post_name = models.CharField(max_length=80)
    rel_date = models.DateField()

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_dur = models.IntegerField()

    def singers(self):
        return ','.join(str(p) for p in self.user.all())


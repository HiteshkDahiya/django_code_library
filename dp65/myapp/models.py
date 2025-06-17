from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_dur = models.IntegerField()

    def singers(self):
        return ','.join([str(p) for p in self.user.all()])
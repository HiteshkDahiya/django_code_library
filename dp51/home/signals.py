from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_success(request,sender,user,**kwargs):
    ct = cache.get('count',0, version=user.pk)
    new_ct = ct + 1
    cache.set('count',new_ct, version=user.pk)
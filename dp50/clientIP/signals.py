from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in,sender=User)
def user_login(request,sender,**kwargs):
    print("-------------------------------")
    print('User get Logged in!!')
    IP = request.META.get('REMOTE_ADDR')
    request.session['ip'] = IP
    print(IP)

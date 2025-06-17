from django.dispatch import receiver,Signal


notification = Signal()

@receiver(notification)
def get_notification(request,sender,user,**kwargs):
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('%')
    print('Get Notificated')
    print(request)
    print(sender)
    print(user)
    print(f'kwargs{kwargs}')
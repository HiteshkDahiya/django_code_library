from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        labels = {'email':'Email'}

class UserEditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        labels = {'email':'Email'}
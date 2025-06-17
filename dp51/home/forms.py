from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control  my-2'}), 'first_name':forms.TextInput(attrs={'class':'form-control  my-2'})
                   , 'last_name':forms.TextInput(attrs={'class':'form-control  my-2'}), 'email':forms.EmailInput(attrs={'class':'form-control  my-2'})}



class LogInForm(AuthenticationForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    class Meta:
        model = User

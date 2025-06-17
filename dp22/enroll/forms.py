from wsgiref.validate import validator

from django import forms


class St(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter your Name'})
    email = forms.EmailField(error_messages={'required': 'Enter your Email'},min_length=10)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Enter your Password'})




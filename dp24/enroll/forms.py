from django import forms
from .models import Data


class St(forms.ModelForm):
    # without modelform class
    # name = forms.CharField(error_messages={'required': 'Aapka Naam likhiye'})
    # email = forms.EmailField(error_messages={'required': 'Enter your Email'},min_length=10)
    # password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Enter your Password'})
    # with modelform class
    class Meta:
        model = Data
        fields = ['name', 'email', 'password']
        error_messages = {'name':{'required':'Enter your name'},'email':{'required':'Enter your email'},
                          'password':{'required':'Enter your password'}}
        widgets = {'password':forms.PasswordInput}
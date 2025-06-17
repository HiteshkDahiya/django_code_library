from django import forms
from .models import DataA


class Student(forms.ModelForm):
    class Meta:
        model = DataA
        fields = ['name', 'email', 'password']
        # fields = '__all__'
        # exclude = ['name']
        error_messages = {'name':{'required':'Enter your name'},'email':{'required':'Enter your email'},
                          'password':{'required':'Enter your password'}}
        widgets = {'password':forms.PasswordInput}
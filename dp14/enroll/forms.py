from django import forms

class St(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
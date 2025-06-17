from django import forms

class St(forms.Form):
    name = forms.CharField(label="Your Name",label_suffix=" =",initial="Santosh",disabled=True,)
    first_name = forms.CharField(help_text="It is a help text")
    email = forms.EmailField()
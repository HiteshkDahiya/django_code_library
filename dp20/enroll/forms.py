from django import forms

def length(value):
    if len(value) < 10:
        raise forms.ValidationError('email too short')          #Custom Validators

class St(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[length])               #Use of Custom Validators
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):                                            #clean() method
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError("name too short")

    def clean_password(self):                                   #clean_fieldName() method
        valpass = self.cleaned_data['password']
        if len(valpass) < 4:
            raise forms.ValidationError("password too short")


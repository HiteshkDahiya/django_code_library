from django import forms

def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError("Name should start with 's'")        #Custom Validators

class St(forms.Form):
    name = forms.CharField(validators=[start_with_s])                    #Use of Custom Validators
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    def clean(self):                                                     #clean() method
        cleaned_data = super().clean()
        valpassword = self.cleaned_data['password']
        rvalpassword = self.cleaned_data['rpassword']
        if valpassword != rvalpassword:
            raise forms.ValidationError("password should match")


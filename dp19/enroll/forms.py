from django import forms

class St(forms.Form):
    name = forms.CharField(min_length=5,max_length=10,error_messages={'required':'Enter you Name','min_length':"Too small"},empty_value='Hitesh')
    roll = forms.IntegerField(min_value=5,max_value=10)
    dnum = forms.DecimalField(min_value=5,max_value=40,max_digits=4,decimal_places=1)
    fnum = forms.FloatField()
    url = forms.URLField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':3,"cols":50}))
    description = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField(label="i agree", label_suffix=" ")
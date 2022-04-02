from django import forms


class SomeForm(forms.Form):
    line1 = forms.CharField(label="Input some info here")
    line2 = forms.CharField(label="Input some info here")
    line3 = forms.CharField(label="Input some info here")


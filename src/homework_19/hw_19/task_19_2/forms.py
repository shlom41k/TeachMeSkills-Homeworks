from django import forms


class SomeData(forms.Form):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

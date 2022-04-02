from django import forms


class OrderForm(forms.Form):
    name = forms.CharField()
    fly_from = forms.CharField()
    fly_to = forms.CharField()
    number_of_passangers = forms.IntegerField()
    fly_date = forms.DateField()

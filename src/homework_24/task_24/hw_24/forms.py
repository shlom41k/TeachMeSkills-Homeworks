from django import forms
from django.core.validators import MinValueValidator, EmailValidator
from .models import NatureImage


class PictureSizeForm(forms.Form):
    height = forms.IntegerField(label="Height",
                                validators=[MinValueValidator(0)])

    weight = forms.IntegerField(label="Weight",
                                validators=[MinValueValidator(0)])


class NatureImageForm(forms.ModelForm):
    class Meta:
        model = NatureImage
        fields = ["link", "height", "weight", "comment"]


class EmailAddressForm(forms.Form):
    e_mail = forms.EmailField(label="E-mail",
                              validators=[EmailValidator()])

    link = forms.CharField(label="Link")

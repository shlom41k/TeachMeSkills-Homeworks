from django import forms
from django.core.validators import MinValueValidator, EmailValidator
from .models import AnimalImage


class AnimalImageForm(forms.ModelForm):
    class Meta:
        model = AnimalImage
        fields = ["url", "type", "pic_type"]
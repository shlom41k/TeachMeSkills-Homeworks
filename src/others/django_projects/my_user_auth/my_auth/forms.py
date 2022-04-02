from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import User


class SigUpForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        required=True,
        label="Login",
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Имя пользователя"
        }),
    )

    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Пароль"
        }),
    )

    repeat_password = forms.CharField(
        required=True,
        label="Repeat password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "ReInputPassword",
            'placeholder': "Повторите пароль"
        }),
    )

    def clean(self):
        super(self.__class__, self).clean()

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            self.add_error("password", "Пароли не совпадают!")

        return self.cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        is_exists = User.objects.filter(username=username)
        if is_exists:
            self.add_error("username", "Пользователь с таким логином уже существует!")
            return None
            # raise forms.ValidationError("Пользователь с таким логином уже существует!")

        user = User.objects.create_user(username=username, password=password)
        user.save()

        # auth = authenticate(**self.cleaned_data)
        # return auth
        return user


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        label="Login",
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )

    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )

    def clean(self):
        super(self.__class__, self).clean()

        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()

        if not user:
            self.add_error("username", "Пользователя с таким именем не существует!")
            return self.cleaned_data

        u = authenticate(**self.cleaned_data)
        if not u:
            self.add_error("password", "Неверный пароль")

        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'city')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'city')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import SigUpForm, SignInForm


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect("home")


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        reg_form = SigUpForm()
        return render(request, "my_auth/register.html", {"form": reg_form})

    def post(self, request, *args, **kwargs):
        reg_form = SigUpForm(request.POST)

        if reg_form.is_valid():
            user = reg_form.save()
            print(user)

            if user is not None:
                # login(request, user)
                return redirect("login")

        return render(request, "my_auth/register.html", {"form": reg_form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = SignInForm()
        return render(request, "my_auth/login.html", {"form": login_form})

    def post(self, request, *args, **kwargs):
        log_form = SignInForm(request.POST)

        if log_form.is_valid():
            user = authenticate(request, **log_form.cleaned_data)

            if user is not None:
                login(request, user)
                return redirect("home")

        messages.error(request, f"Invalid input dada")
        return render(request, "my_auth/login.html", {"form": log_form})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "my_auth/home.html")
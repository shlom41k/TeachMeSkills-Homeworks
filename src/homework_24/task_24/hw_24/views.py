import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import PictureSizeForm, NatureImageForm, EmailAddressForm
from .models import NatureImage


pic_url = "https://picsum.photos/{}/{}"


# Create your views here.
def hw_index(request):

    if request.method == "GET":
        return render(request, "hw_24/index.html", context={"form": PictureSizeForm()})

    elif request.method == "POST":
        form = PictureSizeForm(request.POST)

        if form.is_valid():
            w, h = form.cleaned_data.get("weight"), form.cleaned_data.get("height")
            link = requests.get(pic_url.format(w, h)).url

            f = NatureImageForm(initial={"link": link,
                                         "weight": w,
                                         "height": h})

            return render(request, "hw_24/image.html", context={"form": f})


def image(request):
    if request.method == "POST":
        form = NatureImageForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data.get("link")
            NatureImage(**form.cleaned_data).save()

            email_form = EmailAddressForm(initial={"link": link})

            return render(request, "hw_24/success.html", context={"form": email_form,
                                                                  "link": link})

        return HttpResponse("Invalid form")


def send_to_email(request):
    if request.method == "POST":
        form = EmailAddressForm(request.POST)

        if form.is_valid():
            mail = form.cleaned_data.get("e_mail")
            link = form.cleaned_data.get("link")

            message = f"Link to your image:\n{link}."

            try:
                send_mail("Django image", message, "hw_24@mail.ru", [mail, ])
            except BadHeaderError:
                return HttpResponse('Invalid header')

            return render(request, "hw_24/to_home.html")

        return HttpResponse("Invalid form")

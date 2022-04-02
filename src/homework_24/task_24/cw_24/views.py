import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import AnimalImage
from .forms import AnimalImageForm


dog_url = "https://dog.ceo/api/breeds/image/random"
cat_url = "https://aws.random.cat/meow"


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def pets(request):
    if request.method == 'GET':
        return render(request, "cw_24/index.html")


def get_image(request, pet):
    if request.method == "GET":
        img_url = ""

        if pet not in ["cat", "dog"]:
            return HttpResponse("Unknown pet")

        if pet == "cat":
            data = requests.get(cat_url).json()
            img_url = data.get('file')

        elif pet == "dog":
            data = requests.get(dog_url).json()
            img_url = data.get('message')

        form = AnimalImageForm(initial={"url": img_url,
                                        "type": pet,
                                        "pic_type": img_url.split(".")[-1]})

        return render(request, "cw_24/pet.html", context={"form": form,
                                                          "pet": pet,
                                                          "pic_url": img_url})


def save_image(request):
    if request.method == "POST":

        form = AnimalImageForm(request.POST)

        if form.is_valid():
            try:
                AnimalImage(**form.cleaned_data).save()
                message = f"Image successfully saved"
            except:
                message = f"Image cant be saved"

            return render(request, "cw_24/success.html", context={"message": message})

        return HttpResponse("Invalid form")







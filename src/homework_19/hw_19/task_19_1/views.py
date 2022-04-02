from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

from .forms import SomeForm


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "task_19_1/index.html", {"form": SomeForm()})

    elif request.method == "POST":
        form = SomeForm(request.POST)

        if form.is_valid():
            lines = form.cleaned_data
            return render(request, "task_19_1/result.html", {"max_str": max(list(lines.values()), key=len)})

        return render(request, "task_19_1/index.html", {"form": SomeForm()})

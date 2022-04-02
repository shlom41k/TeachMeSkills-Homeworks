from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .forms import SomeData


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "task_19_2/index.html", {"data": SomeData()})

    elif request.method == "POST":
        form = SomeData(request.POST)

        if form.is_valid():
            # print(form.data["data"])
            return render(request, "task_19_2/result.html", {"data": form.data["data"]})

        return render(request, "task_19_2/index.html", {"data": SomeData()})

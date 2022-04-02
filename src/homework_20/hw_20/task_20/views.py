from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import OrderForm
from datetime import datetime


@csrf_exempt
def order(request):
    if request.method == 'GET':
        return render(request, "task_20/order.html")

    elif request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            tariff = 100
            peoples = form.cleaned_data.get("number_of_passangers")
            data = form.cleaned_data.get("fly_date")
            price = tariff if peoples == 1 else tariff * 2 * peoples

            if datetime.date(datetime.now()) < data:
                return render(request, "task_20/result.html", {"total": price})

        return render(request, "task_20/some_err.html")

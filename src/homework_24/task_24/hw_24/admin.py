from django.contrib import admin
from .models import NatureImage


# Register your models here.
@admin.register(NatureImage)
class NatureImageAdmin(admin.ModelAdmin):
    list_display = ["link", "height", "weight", "comment"]

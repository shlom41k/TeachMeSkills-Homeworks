from django.contrib import admin
from .models import AnimalImage


# Register your models here.
@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    list_display = ["url", "type", "pic_type", "date_of_creating"]

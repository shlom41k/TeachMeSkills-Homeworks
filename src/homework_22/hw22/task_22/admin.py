from django.contrib import admin
from .models import MusicBand, Album, Track


# Register your models here.
@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ["name", "year_of_release", "style"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "year_of_release", "author"]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "album"]

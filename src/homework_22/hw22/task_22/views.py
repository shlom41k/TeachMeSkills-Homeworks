from django.shortcuts import HttpResponse, get_object_or_404
from .models import MusicBand, Album, Track


# Create your views here.
def index(request):
    return HttpResponse("Hello, task 22!")


def albums(request, group):
    band = get_object_or_404(MusicBand, name=group)
    albums = band.albums.all()
    return HttpResponse("<br>".join([f"--> {str(album)}" for album in albums]))


def tracks(request, album: str):
    album = get_object_or_404(Album, name=album)
    tracks = album.tracks.all()
    return HttpResponse("<br>".join([f"--> {str(track)}" for track in tracks]))


def tracks_group(request, group):
    band = get_object_or_404(MusicBand, name=group)
    albums = band.albums.all()
    tracks = []
    for album in albums:
        tr = album.tracks.all()
        tracks.extend([tra for tra in tr])

    return HttpResponse("<br>".join([f"--> {str(track)}" for track in tracks]))
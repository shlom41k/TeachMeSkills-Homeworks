from django.urls import path
from .views import index, albums, tracks, tracks_group


urlpatterns = [
    path('', index, name='index'),
    path('albums/<group>', albums, name='albums'),
    path('tracks/<album>', tracks, name='tracks'),
    path('tracks/group/<group>', tracks_group, name='tracks_group'),
]

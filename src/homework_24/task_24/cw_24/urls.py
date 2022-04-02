from django.urls import path
from .views import index, pets, get_image, save_image


urlpatterns = [
    path('', index, name='index'),
    path('pets/', pets, name='pets'),
    path('pets/<pet>/', get_image, name='get_image'),
    path('pets/save', save_image, name='save_image'),
]

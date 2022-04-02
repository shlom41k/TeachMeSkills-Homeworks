from django.urls import path
from .views import hw_index, image, send_to_email


urlpatterns = [
    path("", hw_index, name="home"),
    path("image/", image, name="image"),
    path("send/", send_to_email, name="send_to_email"),
]

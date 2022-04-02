from django.urls import path
from . import views


urlpatterns = [
   path(r'order/', views.order, name='order'),
]

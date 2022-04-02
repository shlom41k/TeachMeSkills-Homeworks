from django.urls import path
from . import views


urlpatterns = [
   path(r'task2/', views.index, name='task2_index'),
]

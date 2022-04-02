from django.urls import path
from . import views


urlpatterns = [
   path(r'task1/', views.index, name='task1_index'),
]

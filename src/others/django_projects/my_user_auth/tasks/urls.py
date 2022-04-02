from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .views import TaskView, TaskDetailView, TaskCreateView, CommentView


urlpatterns = [
    path('tasks/', TaskView.as_view(), name="tasks"),
    path('tasks/<int:task_id>', TaskDetailView.as_view(), name="task_detail"),
    path('create/', TaskCreateView.as_view(), name="task_create"),

    path('comments/', login_required(CommentView.as_view()), name="comments"),
]

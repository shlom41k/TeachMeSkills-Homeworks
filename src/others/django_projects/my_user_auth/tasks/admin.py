from django.contrib import admin
from .models import Task, Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "creator", "date_of_creating", "executor", "status"]
    list_editable = ["status"]


@admin.register(Comment)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "text", "task"]
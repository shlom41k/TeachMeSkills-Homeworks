from django.contrib import admin
from .models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # fields = ["id", "firstname", "lastname", "age", "test"]
    list_display = ["id", "firstname", "lastname", "age", "test"]
    list_editable = ["test"]
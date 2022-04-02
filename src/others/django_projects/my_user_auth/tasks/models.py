from django.db import models
from django.shortcuts import reverse
from my_auth.models import User


# Модель задачи
class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Task name")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_tasks", null=True, verbose_name="Task creator")
    date_of_creating = models.DateTimeField(verbose_name="Date of creating", auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="executing_tasks", verbose_name="Task executor")

    CREATED = "Created"
    IN_WORK = "In work"
    COMPLETED = "Completed"
    CLOSED = "Closed"

    STATUSES = [
        (CREATED, "Created"),
        (IN_WORK, "In work"),
        (CLOSED, "Closed"),
        (COMPLETED, "Completed"),
    ]
    status = models.CharField(max_length=10, verbose_name="Status", choices=STATUSES, default=CREATED)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("task_detail", args=[self.pk])


# Модель комментария
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET("Unknown user"), related_name="comments", verbose_name="User")
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments", verbose_name="Task")
    text = models.CharField(verbose_name="Comment", max_length=200, blank=True)

    def __str__(self):
        return self.text

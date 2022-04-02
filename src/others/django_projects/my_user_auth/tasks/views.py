from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Task, Comment
from .forms import TaskStatusForm, TaskCreateForm, CommentForm


class TaskView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        created_tasks = Task.objects.filter(creator=request.user)
        executing_tasks = Task.objects.filter(executor=request.user)

        return render(request, "tasks/tasks_all.html", context={
            "created_tasks": created_tasks,
            "executing_tasks": executing_tasks,
        })


class TaskDetailView(View):
    @method_decorator(login_required)
    def get(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)

        if request.user not in [task.creator, task.executor]:
            return redirect("tasks")

        comment_form = CommentForm()

        return render(request, "tasks/task_detail.html", context={
            "task": task,
            "comment_form": comment_form,
        })

    @method_decorator(login_required)
    def post(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)

        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            if text:
                comment = Comment(user=request.user, task=task, text=text)
                comment.save()

                return redirect("task_detail", task_id=task_id)

        if task:
            message = ""

            if task.creator == request.user:
                task.status = Task.CLOSED
                message = f"Task #{task.pk} closed by creator."

            elif task.status == task.CREATED:
                task.status = task.IN_WORK
                message = f"Task #{task.pk} accepted for work."

            elif task.status == task.IN_WORK:
                task.status = task.COMPLETED
                message = f"Task #{task.pk} completed."

            if message:
                task.save()
                comment = Comment(user=request.user, task=task, text=message)
                comment.save()

        return redirect("task_detail", task_id=task_id)


class TaskCreateView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = TaskCreateForm()
        return render(request, "tasks/task_create.html", context={"form": form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            new_task = Task(**form.cleaned_data, creator=request.user, status=Task.CREATED)
            new_task.save()
            comment = Comment(user=request.user, task=new_task, text=f"Task #{new_task.pk} was created")
            comment.save()

        return redirect("tasks")


class CommentView(View):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(user=request.user)
        return render(request, "tasks/comments_all.html")


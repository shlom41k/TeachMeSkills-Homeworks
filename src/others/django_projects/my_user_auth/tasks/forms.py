from django import forms

from .models import Task, Comment


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["status"]


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "executor"]
        widgets = {'name': forms.Textarea(attrs={'cols': 60, 'rows': 10})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {'text': forms.Textarea(attrs={'cols': 60, 'rows': 5})}
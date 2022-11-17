"""Tasks models."""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='created_tasks_set',
    )
    implementer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='assigned_tasks_set',
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label, through='TaskAndLabel')
    date_created = models.DateTimeField(default=timezone.now)


class TaskAndLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

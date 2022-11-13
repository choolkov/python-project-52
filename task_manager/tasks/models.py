"""Tasks models."""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from task_manager.statuses.models import Status


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
    date_created = models.DateTimeField(default=timezone.now)

'''Task filters.'''

import django_filters
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    implementer = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_('Implementer'),
    )
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
    )

    def filter_my_tasks(self, queryset, name, value):
        author = self.request.user
        if value:
            queryset = queryset.filter(author=author)
        return queryset

    my_tasks = django_filters.BooleanFilter(
        label=_("Only my tasks"),
        method="filter_my_tasks",
        widget=forms.CheckboxInput(),
    )

"""Tasks forms."""
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = [
            'author',
            'date_created',
        ]
        localized_fields = (
            'name',
            'implementer',
            'description',
            'status',
            )
        labels = {
            'name': _('Name'),
            'implementer': _('Implementer'),
            'description': _('Description'),
            'status': _('Status'),
            }

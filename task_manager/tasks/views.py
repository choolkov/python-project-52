from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class TaskListView(ListView):
    queryset = Task.objects.all()
    template_name = 'tasks/list.html'


class TaskView(ListView):  # TODO
    queryset = Task.objects.all()
    template_name = 'tasks/list.html'


class CreateTaskView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('The task is successfully created')


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('The task is successfully changed')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('The task is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )

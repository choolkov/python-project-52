from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from django_filters.views import FilterView

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.tasks.filters import TaskFilter
from task_manager.users.mixins import AuthorRequiredMixin


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/preview.html'

class TaskListView(FilterView):
    queryset = Task.objects.all()
    template_name = 'tasks/list.html'
    model = Task
    filterset_class = TaskFilter


class CreateTaskView(SuccessMessageMixin, CreateView):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

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


class DeleteTaskView(
    LoginRequiredMixin, AuthorRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('The task is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )
    failure_url = reverse_lazy("tasks:list")
    failure_message = _("The task can only be deleted by its author.")

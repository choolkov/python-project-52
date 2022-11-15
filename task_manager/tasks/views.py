from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/preview.html'


class TaskListView(ListView):
    queryset = Task.objects.all()
    template_name = 'tasks/list.html'


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


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('The task is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )

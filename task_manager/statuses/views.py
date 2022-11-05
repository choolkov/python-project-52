from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusListView(ListView):
    queryset = Status.objects.all()
    template_name = 'statuses/list.html'


class CreateStatusView(SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:list')
    success_message = _('The status is successfully created')


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:list')
    success_message = _('The status is successfully changed')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:list')
    success_message = _('The status is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )

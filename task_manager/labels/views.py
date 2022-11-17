from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class LabelListView(ListView):
    queryset = Label.objects.all()
    template_name = 'labels/list.html'


class CreateLabelView(SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('The label is successfully created')


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('The label is successfully changed')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )


class DeleteLabelView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('The label is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )

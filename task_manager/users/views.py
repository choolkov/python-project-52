from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.users.forms import UserForm


class UserListView(ListView):
    queryset = User.objects.filter(is_staff=False)
    template_name = 'users/list.html'


class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('The user is successfully registered')


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')
    success_message = _('The user is successfully changed')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )


class DeleteUserView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = _('The user is successfully deleted')
    permission_denied_message = _(
        'You are not authorized! Please complete the entrance.',
    )

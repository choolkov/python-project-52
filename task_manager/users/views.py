from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from task_manager.users.forms import UserForm


class UserListView(ListView):
    queryset = User.objects.filter(is_staff=False)
    template_name = 'users/list.html'


class RegistrationView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

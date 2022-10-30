"""Task Manager views."""

from django.contrib.auth.models import User
from django.views.generic.list import ListView


class UserListView(ListView):
    queryset = User.objects.filter(is_staff=False)
    template_name = 'user_list.html'

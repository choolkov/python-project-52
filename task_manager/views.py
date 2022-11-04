"""Task Manager views."""

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class MessageMixin(object):
    """Add the message to any View descendants."""

    message = ''

    def dispatch(self, request, *args, **kwargs):
        if self.message:
            messages.info(request, self.message)
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = 'index'
    success_message = _('You are logged in')


class UserLogoutView(MessageMixin, LogoutView):
    next_page = 'index'
    message = _('You are logged out')

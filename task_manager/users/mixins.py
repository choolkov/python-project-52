from django.contrib import messages
from django.shortcuts import redirect
from django.core import exceptions


class AuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        author_id = self.model.objects.get(pk=self.kwargs.get('pk')).author
        if author_id != self.request.user:
            if self.failure_message:
                messages.error(self.request, self.failure_message)
            if not self.failure_url:
                raise exceptions.ImproperlyConfigured
            return redirect(self.failure_url)
        return super().dispatch(request, *args, **kwargs)

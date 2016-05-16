from django.http import Http404

__author__ = 'mrk2'
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class StaftRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(StaftRequiredMixin, self).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(StaftRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

class LoginRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(LoginRequiredMixin, self).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


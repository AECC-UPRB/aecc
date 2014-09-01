from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, ListView, DetailView
from django.http import Http404
from django.conf import settings
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import User, Payment
from .forms import SettingsForm


class DirectiveView(ListView):
    paginate_by = 12
    template_name = 'users/community.html'

    def get_queryset(self):
        return User.objects.filter(
            email__in=Payment.objects.filter(
                amount_payed=settings.AECC_UPRB_MEMBER_FEE,
                year_payed=datetime.now().year).
            order_by('-created_at').values_list('payed_by__email'))


class SettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = "users/settings.html"
    form_class = SettingsForm
    success_message = 'Perfil actualizado.'

    def get_success_url(self):
        return reverse(
            'users:settings',
            kwargs={'slug': self.request.user.slug}
        )

    def get_object(self, *args, **kwargs):
        obj = super(SettingsView, self).get_object(*args, **kwargs)
        if not obj == self.request.user:
            raise Http404
        elif not self.request.user.has_valid_membership():
            raise Http404
        return obj


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'person_profile'

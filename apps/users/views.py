from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, TemplateView, DetailView
from django.http import Http404
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import User
from .forms import SettingsForm


class DirectiveView(TemplateView):
    template_name = 'users/community.html'

    def get_context_data(self, **kwargs):
        context = super(DirectiveView, self).get_context_data(**kwargs)
        context['directive'] = User.objects.filter(amount_payed=15)
        return context


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
        return obj


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'person_profile'

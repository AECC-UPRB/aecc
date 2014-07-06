from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from .models import User
from .forms import SettingsForm


class DirectiveView(TemplateView):
    template_name = 'users/directive.html'

    def get_context_data(self, **kwargs):
        context = super(DirectiveView, self).get_context_data(**kwargs)
        context['directive'] = User.objects.filter(amount_payed=15)
        return context


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "users/settings.html"
    form_class = SettingsForm

    def get_success_url(self):
        return reverse('users:settings')

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs

    def get_initial(self):
        initial = {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'courses': self.request.user.courses,
            'programming_languages': self.request.user.programming_languages,
            'email': self.request.user.email,
            'phone_number': self.request.user.phone_number,
            'facebook': self.request.user.facebook,
            'twitter': self.request.user.twitter,
            'github': self.request.user.github,
            'linkedin': self.request.user.linkedin,
        }
        return initial

    def form_valid(self, form):
        form.save_form(self.request.user)
        messages.success(self.request, 'Perfil actualizado.')
        return redirect(self.get_success_url())

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, ListView, DetailView
from django.http import Http404
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import User
from .forms import SettingsForm


class DirectiveView(ListView):
    model = User
    template_name = 'users/community.html'
    paginate_by = '2'

    def get_context_data(self, **kwargs):
        context = super(DirectiveView, self).get_context_data(**kwargs)
        context['community'] = User.objects.filter(amount_payed=15)
        page = self.request.GET.get('page')
        if page is None:
            context['max_to_present'] = int(self.paginate_by)
            context['start_with'] = 1
            context['current_page'] = 1
        else:
            max_to_present = int(page) * int(self.paginate_by)
            context['max_to_present'] = max_to_present
            context['start_with'] = (max_to_present - int(self.paginate_by)) + 1
            context['current_page'] = int(page)
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

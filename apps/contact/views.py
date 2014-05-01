from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect

from .forms import ContactForm


class IndexView(FormView):
    form_class = ContactForm
    template_name = 'contact/index.html'
    success_url = '/contact/thanks/'

    def form_valid(self, form):
        form.send()
        return redirect(self.get_success_url())


class ThanksView(TemplateView):
    template_name = 'contact/thanks.html'

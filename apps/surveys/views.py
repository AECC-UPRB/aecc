from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from braces.views import LoginRequiredMixin

from .models import Survey, Poll, Choice
from .forms import SurveyForm
from .mixins import SurveySubmittedMixin


class SurveyView(LoginRequiredMixin, SurveySubmittedMixin, FormView):
    template_name = 'surveys/index.html'
    form_class = SurveyForm
    success_url = reverse_lazy('surveys:thanks')

    def get_context_data(self, **kwargs):
        context = super(SurveyView, self).get_context_data(**kwargs)
        context['survey'] = Survey.objects.get(slug=self.kwargs['slug'])
        context['survey_questions'] = Poll.objects.filter(
            survey=context['survey'])
        context['survey_choices'] = Choice.objects.filter(
            poll=context['survey_questions'])
        return context

    def post(self, request, **kwargs):
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.kwargs['post_data'] = self.request.POST
        form.save_form(self.request.user.id, **self.kwargs)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ThanksView(TemplateView):
    template_name = 'surveys/thanks.html'

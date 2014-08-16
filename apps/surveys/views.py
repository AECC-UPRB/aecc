from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages

from braces.views import LoginRequiredMixin

from .models import Survey, Poll, Choice
from .mixins import SurveySubmittedMixin


class SurveyView(LoginRequiredMixin, SurveySubmittedMixin, FormView):
    template_name = 'surveys/index.html'
    success_url = reverse_lazy('surveys:thanks')
    object = None

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
        self.object = Survey.objects.get(slug=self.kwargs['slug'])
        if not self.request.user in self.object.sent_by.all():
            questions = Poll.objects.filter(survey=self.object)
            for q in questions:
                try:
                    c = q.choice_set.get(
                        pk=self.request.POST["choice"+str(q.id)])
                    c.votes += 1
                    c.save()
                    self.object.save()
                except (KeyError, Choice.DoesNotExist):
                    messages.error(
                        self.request,
                        'Please select a choice for each question.')
                    return self.render_to_response(
                        self.get_context_data(form=form))
            self.object.sent_by.add(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class ThanksView(TemplateView):
    template_name = 'surveys/thanks.html'

from django.shortcuts import Http404, redirect
from django.views.generic import FormView

from .models import Survey, Poll, Choice
from .forms import SurveyForm


# TODO - Change ListView to FormView and implement post method
class SurveyView(FormView):
    template_name = "surveys/index.html"
    form_class = SurveyForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        survey_object = Survey.objects.filter(slug=self.kwargs['slug'])
        poll_object = Poll.objects.filter(survey=survey_object)
        context = super(SurveyView, self).get_context_data(**kwargs)
        context['survey'] = Survey.objects.get(id=survey_object)
        context['survey_questions'] = Poll.objects.filter(survey=survey_object)
        context['survey_choices'] = Choice.objects.filter(poll=poll_object)
        return context

    def post(self, request, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            self.kwargs['post_data'] = self.request.POST
            valid = form.save_form(self.request.user.id, **self.kwargs)
            if valid:
                return redirect('index')
            else:
                raise Http404

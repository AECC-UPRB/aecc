from django.views.generic import ListView

from .models import Survey, Poll, Choice


class SurveyView(ListView):
    model = Survey
    template_name = "surveys/index.html"
    slug_field = 'slug'
    context_object_name = 'survey_data'

    def get_queryset(self):
        return Survey.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        survey_object = Survey.objects.filter(slug=self.kwargs['slug'])
        poll_object = Poll.objects.filter(survey=survey_object)
        context = super(SurveyView, self).get_context_data(**kwargs)
        context['survey_questions'] = Poll.objects.filter(survey=survey_object)
        context['survey_choices'] = Choice.objects.filter(poll=poll_object)
        return context

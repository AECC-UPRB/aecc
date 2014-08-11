from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from .models import Survey, Poll, Choice

# TODO - Change ListView to FormView and implement post method
class SurveyView(ListView):
    model = Survey
    template_name = "surveys/index.html"
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        survey_object = Survey.objects.filter(slug=self.kwargs['slug'])
        poll_object = Poll.objects.filter(survey=survey_object)
        context = super(SurveyView, self).get_context_data(**kwargs)
        context['survey'] = Survey.objects.get(id=survey_object)
        context['survey_questions'] = Poll.objects.filter(survey=survey_object)
        context['survey_choices'] = Choice.objects.filter(poll=poll_object)
        return context


# TODO Logic goes to "SurveyForm"
def vote(request, slug):
    s = get_object_or_404(Survey, slug=slug)
    p = Poll.objects.filter(survey=s)
    for questions_votes in p:
        choice = 'choice' + str(questions_votes.id)
        c = get_object_or_404(
            Choice, pk=request.POST[choice], poll=questions_votes.id)
        c.votes += 1
        c.save()
    s.sent_by.add(request.user.id)
    s.save()
    return redirect('/blog')

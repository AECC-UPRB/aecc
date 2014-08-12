from django import forms
from django.shortcuts import get_object_or_404

from .models import Survey, Poll, Choice


class SurveyForm(forms.Form):

    def save_form(self, user, **kwargs):
        s = get_object_or_404(Survey, slug=kwargs['slug'])
        if not user in s.sent_by.all():
            p = Poll.objects.filter(survey=s)
            for questions_votes in p:
                try:
                    c = get_object_or_404(
                        Choice, pk=kwargs['post_data']['choice' + str(questions_votes.id)], poll=questions_votes.id)

                except (KeyError, Choice.DoesNotExist):
                    return False
                else:
                    c.votes += 1
                    c.save()
                    s.sent_by.add(user)
                    s.save()
                    return True

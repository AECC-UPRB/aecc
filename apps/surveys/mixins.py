from django.shortcuts import redirect

from .models import Survey


class SurveySubmittedMixin(object):

    def get(self, request, *args, **kwargs):
        if request.user in Survey.objects.get(
                slug=self.kwargs['slug']).sent_by.all():
            return redirect('index')
        return self.render_to_response(self.get_context_data())

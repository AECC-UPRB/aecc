from django.shortcuts import redirect

from .models import Survey


class SurveySubmittedMixin(object):

    def get(self, request, *args, **kwargs):
        print self.kwargs['slug']
        if request.user in Survey.objects.get(
                slug=self.kwargs['slug']).sent_by.all():
            return redirect('index')
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

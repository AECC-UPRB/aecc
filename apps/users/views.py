from django.views.generic import TemplateView

from .models import User


class DirectiveView(TemplateView):
    template_name = 'users/directive.html'

    def get_context_data(self, **kwargs):
        context = super(DirectiveView, self).get_context_data(**kwargs)
        context['directive'] = User.objects.all()
        return context

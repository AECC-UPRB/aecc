from datetime import datetime

from django.views.generic import TemplateView

from apps.events.models import Event


class HomeView(TemplateView):
    template_name = 'static/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            event_date__gt=datetime.now()).order_by('event_date')[:2]
        return context

from django.views.generic import ListView, DetailView

from .models import Event
from .mixins import MonthMixin


class IndexView(MonthMixin, ListView):
    model = Event
    paginate_by = 5
    template_name = 'events/index.html'
    context_object_name = 'events_information'


class EventView(DetailView):
    model = Event
    slug_field = 'title_slug'
    slug_url_kwarg = 'title_slug'
    template_name = 'events/event.html'
    context_object_name = 'event'


class EventByMonth(ListView):
    model = Event
    paginate_by = 5
    context_object_name = 'events'
    template_name = 'events/events_by_month.html'

    def get_queryset(self):
        return Event.objects.filter(month=self.kwargs['month'])

    def get_context_data(self, **kwargs):
        context = super(EventByMonth, self).get_context_data(**kwargs)
        context['month'] = self.kwargs['month']
        return context

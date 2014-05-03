from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404

from .models import Event


class IndexView(ListView):
    model = Event
    paginate_by = 5
    queryset = Event.objects.all().order_by('-event_date')
    template_name = 'events/index.html'
    context_object_name = 'events_information'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                  'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER',
                  'DECEMBER']
        context['months'] = months
        return context


class EventView(DetailView):
    model = Event
    slug_field = 'title_slug'
    slug_url_kwarg = 'title_slug'
    template_name = 'events/event.html'
    context_object_name = 'event'


class EventByMonth(ListView):
    model = Event
    template_name = 'events/events_by_month.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        return get_list_or_404(
            Event,
            month_slug=self.kwargs['month'])

from django.views.generic import ListView, DetailView

from .models import Event


class IndexView(ListView):
    model = Event
    paginate_by = 5
    queryset = Event.objects.all().order_by('-event_date')
    template_name = 'events/index.html'
    context_object_name = 'events_information'

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                  'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER',
                  'DECEMBER']
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(
                queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
            context['months'] = months
        context.update(kwargs)
        return super(IndexView, self).get_context_data(**context)


class EventView(DetailView):
    model = Event
    slug_field = 'title_slug'
    template_name = 'events/event.html'
    context_object_name = 'event'


class EventByMonth(ListView):
    model = Event
    paginate_by = 5
    template_name = 'events/events_by_month.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(
            month_slug=self.kwargs['event_month']).order_by('-event_date')

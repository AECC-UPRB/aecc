from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Events


def events_view(request):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    data = {
        'events_information': Events.objects.all(),
        'months': months
    }
    return render(request, 'events/events.html', data)


def event(request, title_slug):
    event = get_object_or_404(Events, title_slug=title_slug)
    data = {
        'event': Events.objects.get(id=event.id)
    }
    return render(request, 'events/event.html', data)


def events_by_month(request, event_month):
    months_events = get_object_or_404(Events, month_slug=event_month)
    data = {
        'event': months_events,
        'month_specified': event_month
    }
    return render(request, 'events/events_by_month.html', data)

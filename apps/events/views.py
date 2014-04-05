from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

from .models import Events


def events_view(request):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    data = {
        'events_information': Events.objects.all(),
        'months': months
    }
    return render_to_response('events.html', data)


def event(request, slug):
    event = get_object_or_404(Events, slug=slug)
    data = {
        'event': Events.objects.get(id=event.id)
    }
    return render_to_response('event.html', data)


def events_by_month(request, event_month):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    hit = event_month.upper() in months
    if hit == 1:
        data = {
            'events': Events.objects.filter(month=event_month),
            'month_specified': event_month
        }
        return render_to_response('events_by_month.html', data)
    else:
        raise Http404

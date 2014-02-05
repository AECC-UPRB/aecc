from django.http import Http404
from django.shortcuts import render_to_response

from events.models import Events


def events_view(request):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    data = {
        'events_information': Events.objects.all(),
        'months': months
    }
    return render_to_response('events.html', data)

def event(request, slug):
    hit = False
    for event in Events.objects.all():
        if event.slug == slug:
            hit = True
            data = {
                'event': Events.objects.get(id=event.id)
            }
            return render_to_response('event.html', data)
    if hit is False:
        raise Http404

def events_by_month(request, event_month):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    hit = event_month.upper() in months
    if hit == 1:
        data = {
            'events': Events.objects.all(),
            'month_specified': event_month
        }
        return render_to_response('events_by_month.html', data)
    else:
        raise Http404

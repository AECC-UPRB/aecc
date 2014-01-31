from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

from events.models import Events


def events_view(request):
    data = {
        'events_information': Events.objects.all()
    }
    return render_to_response('events.html', data)

def event(request, event_id=1):
    data = {
        'event': get_object_or_404(Events, id=event_id)
    }
    return render_to_response('event.html', data)

def event_by_month(request, event_month):
    events_for_month = Events.objects.all()
    hit = False
    for events in events_for_month:
        if events.month.upper() == event_month.upper():
            hit = True
            data = {
                'events_for_month': events,
                'month_specified': event_month
            }
            return render_to_response('events-by-month.html', data)
    if hit is False:
        raise Http404

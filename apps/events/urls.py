from django.conf.urls import patterns, url

from .views import IndexView, EventView, EventByMonth, HackathonView, ParticipatingView
from .feeds import EventCalendarFeed

urlpatterns = patterns(
    '',
    url(
        r'^ical/$',
        EventCalendarFeed(),
        name='event_calendar_feed'
    ),
    url(
        r'^hackathon/$',
        HackathonView.as_view(),
        name='hackathon'
    ),
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^(?P<month>[-\w]+)/$',
        EventByMonth.as_view(),
        name='month'
    ),
    url(
        r'^(?P<month>[\w]+)/(?P<title_slug>[-\w]+)/$',
        EventView.as_view(),
        name='event'
    ),
    # TODO - remove url, causes leak
    url(
        r'^(?P<month>[\w]+)/(?P<title_slug>[-\w]+)/check_in$',
        ParticipatingView.as_view(),
        name='check_in'
    ),
)

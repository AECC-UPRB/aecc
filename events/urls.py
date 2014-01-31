from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'events.views.events_view'),
    url(r'^get/(?P<event_id>\d+)/$', 'events.views.event'),
    url(r'^(?P<event_month>.+)/$', 'events.views.event_by_month'),
)

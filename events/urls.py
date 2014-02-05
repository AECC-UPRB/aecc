from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'events.views.events_view'),
    url(r'^get/(?P<slug>[-_\w]+)/$', 'events.views.event'),
    url(r'^(?P<event_month>.+)/$', 'events.views.events_by_month'),
)

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.events_view, name='index'),
    url(r'^view/(?P<title_slug>[-_\w]+)/$', views.event, name='event'),
    url(r'^(?P<event_month>.+)/$', views.events_by_month, name='event_month'),
)

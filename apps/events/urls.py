from django.conf.urls import patterns, url

from .views import IndexView, EventView, EventByMonth


urlpatterns = patterns(
    '',
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^(?P<title_slug>[-_\w]+)/$',
        EventView.as_view(),
        name='event'
    ),
    url(
        r'^(?P<event_month>.+)/$',
        EventByMonth.as_view(),
        name='event_month'
    ),
)

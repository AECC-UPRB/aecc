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
        r'^(?P<event_month>[\b(january|feburary|march|april|may|june|july|august|september|october|november|december)\w]+)/$',
        EventByMonth.as_view(),
        name='event_month'
    ),
    url(
        r'^(?P<title_slug>[\w-]+)/$',
        EventView.as_view(),
        name='event'
    ),
)

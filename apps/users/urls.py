from django.conf.urls import patterns, url

from .views import DirectiveView


urlpatterns = patterns(
    '',
    url(
        r'^directive/$',
        DirectiveView.as_view(),
        name='directive'
    ),
)

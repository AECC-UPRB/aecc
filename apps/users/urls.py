from django.conf.urls import patterns, url

from .views import DirectiveView
from .views import SettingsView


urlpatterns = patterns(
    '',
    url(
        r'^directive/$',
        DirectiveView.as_view(),
        name='directive'
    ),
    url(
        r'^profile/settings/$',
        SettingsView.as_view(),
        name='settings'
    ),
)

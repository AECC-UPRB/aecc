from django.conf.urls import patterns, url

from .views import DirectiveView
from .views import SettingsView
from .views import ProfileView


urlpatterns = patterns(
    '',
    url(
        r'^community/$',
        DirectiveView.as_view(),
        name='community'
    ),
    url(
        r'^(?P<slug>[-\w]+)/settings/$',
        SettingsView.as_view(),
        name='settings'
    ),
    url(
        r'^(?P<slug>[-\w]+)/profile/$',
        ProfileView.as_view(),
        name='profile'
    ),
)

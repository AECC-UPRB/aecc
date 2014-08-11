from django.conf.urls import patterns, url
from .views import SurveyView, vote

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$', SurveyView.as_view(), name='survey'),
    # TODO - remove url causes leak
    url(r'^(?P<slug>[-\w]+)/vote$', vote, name='vote'),
)

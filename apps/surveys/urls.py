from django.conf.urls import patterns, url
from .views import SurveyView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$', SurveyView.as_view(), name='survey'),
)

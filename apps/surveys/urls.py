from django.conf.urls import patterns, url
from .views import SurveyView, ThanksView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'^(?P<slug>[-\w]+)/$', SurveyView.as_view(), name='survey'),
)

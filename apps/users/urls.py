from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^signup/$', views.signup_view, name='index'),
    url(r'^directive/$', views.directive_view, name='directive'),
)

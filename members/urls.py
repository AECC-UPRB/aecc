from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'members.views.signup_view'),
)

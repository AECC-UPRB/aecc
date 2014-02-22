from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'users.views.signup_view'),
)

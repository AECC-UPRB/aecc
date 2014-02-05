from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^$', 'contact.views.contact_us_view'),
)

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'people.views.people_view'),
)
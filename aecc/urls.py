from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('apps.events.urls', namespace='events')),
    url(r'^people/', include('apps.people.urls', namespace='people')),
    url(r'^contact/', include('apps.contact.urls', namespace='contact')),
    url(r'^signup/', include('apps.members.urls', namespace='members')),

    # static pages
    url(r'^/$', TemplateView.as_view(
        template_name='static/index.html'), name='index'),
    url(r'^about/$', TemplateView.as_view(
        template_name='static/about.html'), name='about'),
)

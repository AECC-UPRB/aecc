from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # static pages
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^about/$', TemplateView.as_view(
        template_name='static/about.html'), name='about'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^events/', include('apps.events.urls', namespace='events')),
    url(r'^contact/', include('apps.contact.urls', namespace='contact')),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^members/', include('apps.users.urls', namespace='users')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

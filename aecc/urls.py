from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'aecc.views.home_view'),
    url(r'^home/$', 'aecc.views.home_view'),
    url(r'^about/$', 'aecc.views.about_view'),
    url(r'^events/', include('apps.events.urls')),
    url(r'^people/', include('apps.people.urls')),
    url(r'^contact/', include('apps.contact.urls')),
    url(r'^signup/', include('apps.members.urls'))
)

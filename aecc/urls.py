from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'aecc.views.home_view'),
    url(r'^home/$', 'aecc.views.home_view'),
    url(r'^about/$', 'aecc.views.about_view'),
    url(r'^events/', include('events.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^signup/', include('members.urls'))
)

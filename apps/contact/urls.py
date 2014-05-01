from django.conf.urls import patterns, url

from .views import IndexView, ThanksView

urlpatterns = patterns(
    '',
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^thanks/$',
        ThanksView.as_view(),
        name='thanks'
    ),
)

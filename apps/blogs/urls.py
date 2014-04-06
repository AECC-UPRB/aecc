from django.conf.urls import patterns, url

from .views import blogs_view, branch_articles_view, article_view

urlpatterns = patterns(
    '',
    url(r'^$', blogs_view, name='blogs'),
    url(r'^(?P<branch_slug>[-_\w]+)/$',
        branch_articles_view, name="specified_branch"),
    url(r'^(?P<branch_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)$',
        article_view, name="specified_article"),
)

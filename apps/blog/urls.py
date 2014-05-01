from django.conf.urls import patterns, url

from .views import IndexView, BranchArticlesView, ArticleView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^(?P<branch_slug>[-_\w]+)/$',
        BranchArticlesView.as_view(),
        name="branch"
    ),
    url(
        r'^(?P<branch_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$',
        ArticleView.as_view(),
        name="article"
    ),
)

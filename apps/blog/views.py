from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Article


class IndexView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'blog/index.html'
    queryset = Article.objects.all()[:5]


class BranchArticlesView(ListView):
    model = Article
    template_name = 'blog/branch_articles.html'
    context_object_name = 'branch_articles'
    paginate_by = 5

    def get_queryset(self):
        return get_list_or_404(
            Article,
            branch_slug=self.kwargs['branch_slug'])


class ArticleView(DetailView):
    model = Article
    slug_field = 'article_slug'
    slug_field_kwarg = 'article_slug'
    template_name = 'blog/article.html'
    context_object_name = 'article'

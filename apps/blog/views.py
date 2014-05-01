from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Article


class IndexView(ListView):
    model = Article
    paginate_by = 5
    queryset = Article.objects.all().order_by('-created_at')
    template_name = 'blog/index.html'


class BranchArticlesView(DetailView):
    model = Article
    slug_field = 'branch_slug'
    template_name = 'blog/branch_articles.html'
    context_object_name = 'branch'

    def get_queryset(self):
        return Article.objects.filter(branch_slug=self.kwargs['branch_slug'])


class ArticleView(DetailView):
    model = Article
    slug_field = 'branch_slug'
    template_name = 'blog/article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['article'] = get_object_or_404(
            Article,
            branch_slug=kwargs['branch_slug'],
            article_slug=kwargs['article_slug'])
        return kwargs

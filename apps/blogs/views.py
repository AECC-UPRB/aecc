from django.shortcuts import render, get_object_or_404

from .models import Article


def blogs_view(request):
    render(request, 'blogs/blogs.html')

def branch_articles_view(request, branch_slug):
    specified_branch = get_object_or_404(Article, branch_slug=branch_slug)
    data = {
        'branch': specified_branch
    }
    render(request, 'blogs/branch_articles.html', data)

def article_view(request, branch_slug, article_slug):
    article = get_object_or_404(Article, branch_slug=branch_slug, article_slug=article_slug)
    data = {
        'article': article
    }
    return render(request, 'blogs/article.html', data)

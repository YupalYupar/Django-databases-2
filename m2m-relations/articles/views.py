from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    query_set = '-published_at'
    articles = Article.objects.all().order_by(query_set)

    context = {'object_list': articles}
    return render(request, template, context)

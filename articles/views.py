from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles_view(request):
    articles = Article.objects.all()
    context = {"articles": articles}

    return render(request, 'article/articles.html',context)

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        "form": form,
    }
    return render(request, "article/create.html", context)

def article_edit_view(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()

    context = {
        "form": form,
        "article": article
    }

    return render(request, "article/edit.html", context)

def article_detail_view(request, id):
    article = Article.objects.get(id=id)

    context = {"article":article}
    return render(request, "article/detail.html", context)

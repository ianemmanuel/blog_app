from django.shortcuts import render
from articles.models import Article
# Create your views here.

def home_view(request):
    articles = Article.objects.all().order_by('-id')[:3]
    context = {"articles": articles}

    return render(request, "pages/home.html", context)

def contacts_view(request):
    context = {}
    return render(request, "pages/contact.html", context)

def about_view(request):
    context = {}
    return render(request, "pages/about.html", context)


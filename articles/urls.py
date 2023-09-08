from django.contrib import admin
from django.urls import path
from .views import article_create_view, article_edit_view, article_detail_view, articles_view


app_name= 'articles'
urlpatterns = [
    path('', articles_view,name="articles"),
    path('create/', article_create_view, name="create"),
    path('edit/<int:id>/', article_edit_view, name="edit"),
    path('<int:id>/', article_detail_view, name="detail"),
]

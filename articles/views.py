from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'body']

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = '/articles/'


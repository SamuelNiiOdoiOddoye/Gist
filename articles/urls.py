from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('',ArticleListView.as_view(), name='articles_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
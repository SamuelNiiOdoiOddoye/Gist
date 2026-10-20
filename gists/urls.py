from django.urls import path
from .views import GistsListView, GistDetailView, GistCreateView, GistUpdateView, GistDeleteView

urlpatterns = [
    path('',GistsListView.as_view(), name='gists_list'),
    path('<int:pk>/', GistDetailView.as_view(), name='gist_detail'),
    path('create/', GistCreateView.as_view(), name='gist_create'),
    path('<int:pk>/update/', GistUpdateView.as_view(), name='gist_update'),
    path('<int:pk>/delete/', GistDeleteView.as_view(), name='gist_delete'),
]
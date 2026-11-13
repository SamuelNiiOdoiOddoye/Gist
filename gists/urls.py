
from django.urls import path

from .views import (
    GistsListView,
    GistDetailView,
    GistCreateView,
    GistUpdateView,
    GistDeleteView,
    GistCommentCreateView,
)


urlpatterns = [
    # Display all gists.
    path(
        "",
        GistsListView.as_view(),
        name="gists_list",
    ),

    # Display one gist.
    path(
        "gist/<int:pk>/",
        GistDetailView.as_view(),
        name="gist_detail",
    ),

    # Create a new gist.
    path(
        "gist/new/",
        GistCreateView.as_view(),
        name="gist_create",
    ),

    # Update an existing gist.
    path(
        "gist/<int:pk>/update/",
        GistUpdateView.as_view(),
        name="gist_update",
    ),

    # Delete an existing gist.
    path(
        "gist/<int:pk>/delete/",
        GistDeleteView.as_view(),
        name="gist_delete",
    ),

    # Add a comment to a particular gist.
    path(
        "gist/<int:pk>/comment/",
        GistCommentCreateView.as_view(),
        name="gist_comment_create",
    ),
]

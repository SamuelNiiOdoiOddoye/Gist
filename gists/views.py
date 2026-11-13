
from typing import cast

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import GistCommentForm
from .models import Gist, GistComment


class GistsListView(ListView):
    """
    Displays a list of all gists.

    The template can access the queryset using the
    context variable 'gists'.
    """

    model = Gist
    template_name = "gists/gists_list.html"
    context_object_name = "gists"
    ordering = ["-date_posted"]


class GistDetailView(LoginRequiredMixin, DetailView):
    """
    Displays the details of a single gist.

    LoginRequiredMixin ensures that only authenticated
    users can access this page.
    """

    model = Gist
    template_name = "gists/gist_detail.html"
    context_object_name = "gist"


class GistCreateView(LoginRequiredMixin, CreateView):
    """
    Allows an authenticated user to create a gist.

    The currently logged-in user is automatically assigned
    as the author.
    """

    model = Gist
    template_name = "gists/gist_create.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        # ModelForm's instance is typed generically.
        # cast() tells Pylance that this instance is a Gist.
        gist = cast(Gist, form.instance)

        # Assign the logged-in user as the author.
        # Users cannot choose another author through the form.
        gist.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the newly created gist after saving.

        getattr() avoids Pylance warnings about accessing
        self.object before Django's generic view typing
        recognises that attribute.
        """

        gist = cast(
            Gist | None,
            getattr(self, "object", None),
        )

        if gist is None:
            return reverse("gists_list")

        return reverse(
            "gist_detail",
            kwargs={"pk": gist.pk},
        )


class GistUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    """
    Allows only the original author to update a gist.
    """

    model = Gist
    template_name = "gists/gist_update.html"
    fields = ["title", "body"]

    def test_func(self):
        """
        Check whether the logged-in user owns this gist.

        If the user is not the author, Django denies access.
        """

        gist = cast(Gist, self.get_object())

        return self.request.user == gist.author


class GistDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    """
    Allows only the original author to delete a gist.
    """

    model = Gist
    template_name = "gists/gist_delete.html"
    success_url = reverse_lazy("gists_list")

    def test_func(self):
        """
        Confirm that the logged-in user owns the gist
        before allowing deletion.
        """

        gist = cast(Gist, self.get_object())

        return self.request.user == gist.author


class GistCommentCreateView(LoginRequiredMixin, CreateView):
    """
    Allows an authenticated user to comment on a gist.

    The author and associated gist are assigned by the
    application rather than being supplied by the user.
    """

    model = GistComment
    form_class = GistCommentForm
    template_name = "gists/gist_comment_form.html"

    def form_valid(self, form):
        """
        Assign the comment's author and associated gist
        before Django saves the comment.
        """

        comment = cast(GistComment, form.instance)

        # Associate the comment with the currently
        # authenticated user.
        comment.comment_author = self.request.user

        # Associate the comment with the gist identified
        # by the primary key in the URL.
        comment.comment_gist = get_object_or_404(
            Gist,
            pk=self.kwargs["pk"],
        )

        # Django now saves the completed comment.
        return super().form_valid(form)

    def get_success_url(self):
        """
        After creating a comment, return to the gist
        that the user commented on.
        """

        comment = cast(
            GistComment | None,
            getattr(self, "object", None),
        )

        if comment is None:
            return reverse("gists_list")

        return reverse(
            "gist_detail",
            kwargs={"pk": comment.comment_gist.pk},
        )

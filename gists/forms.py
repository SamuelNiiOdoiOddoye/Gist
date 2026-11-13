
from django import forms

from .models import GistComment


class GistCommentForm(forms.ModelForm):
    """
    Form for creating a comment on a gist.

    The user only supplies the comment body.
    The view assigns the author and associated gist.
    """

    class Meta:
        model = GistComment

        # Do not expose comment_author or comment_gist.
        # These are assigned securely in the view.
        fields = ("comment_body",)

        widgets = {
            "comment_body": forms.Textarea(
                attrs={
                    "placeholder": "Write your comment...",
                    "rows": 4,
                    "class": "form-control",
                }
            ),
        }

        labels = {
            "comment_body": "Your comment",
        }

from django.contrib import admin
from .models import GistComment, Gist

class GistCommentInline(admin.StackedInline):
    model = GistComment
    
    # Display 1 blank form for adding a new comment in the Gist admin page.
    extra =1

class GistAdmin(admin.ModelAdmin):
    inlines=[
        GistCommentInline,
    ]

# Register your models here.
admin.site.register(Gist, GistAdmin)
admin.site.register(GistComment)

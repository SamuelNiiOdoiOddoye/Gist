from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Gist(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_dislikes', blank=True)
    reposts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_reposts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gist_detail', kwargs={'pk': self.pk})
    
class GistComment(models.Model):
    comment_gist = models.ForeignKey(Gist, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date_posted = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    comment_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_comment_likes', blank=True)
    comment_dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_comment_dislikes', blank=True)
    comment_reposts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='gist_comment_reposts', blank=True)

    def __str__(self):
        return f'Comment by {self.comment_author.username} on {self.comment_gist.title}'
    
    def get_absolute_url(self):
        return reverse('gist_detail', kwargs={'pk': self.comment_gist.pk})
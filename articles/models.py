from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_dislikes', blank=True)
    reposts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_reposts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
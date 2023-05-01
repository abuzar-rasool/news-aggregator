from django.db import models

from django.db import models
from django.contrib.auth.models import User

class NewsItem(models.Model):
    headline = models.CharField(max_length=255, null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    source = models.CharField(max_length=100, null=False, blank=False)

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class CachedNewsItem(models.Model):
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE)
    query = models.CharField(max_length=255, null=True, blank=False)
    last_fetched = models.DateTimeField(null=False, blank=False)




from datetime import datetime, timedelta
from typing import List

from django.db import transaction

from .cache_fetcher import CacheFetcher
from core.models import NewsItem, CachedNewsItem
from django.utils import timezone


DEFAULT_EXPIRATION_TIME = 60

class DatabaseCacheFetcher(CacheFetcher):
    def __init__(self, expiration_time=DEFAULT_EXPIRATION_TIME):
        self.expiration_time = expiration_time
        
    def fetch(self, query=None):
        cache = CachedNewsItem.objects.filter(query=query, last_fetched__gte=timezone.now()-timedelta(seconds=self.expiration_time))
        news_items = [item.news_item for item in cache]
        if cache.exists():
            cache.update(last_fetched=timezone.now())
            return news_items
        else:
            return None
    
    def store(self, news_items, query=None):
        result = []
        with transaction.atomic():
            for news_item in news_items:
                updated_news_item, created = NewsItem.objects.get_or_create(headline=news_item.headline, link=news_item.link, source=news_item.source)
                result.append(updated_news_item)
            CachedNewsItem.objects.filter(query=query).delete()
            CachedNewsItem.objects.bulk_create([CachedNewsItem(news_item=item, query=query, last_fetched=timezone.now()) for item in result])
        return result

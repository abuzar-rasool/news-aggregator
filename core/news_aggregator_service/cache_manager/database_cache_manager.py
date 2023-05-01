from datetime import datetime, timedelta
from typing import List

from django.db import transaction

from .cache_manager import CacheManager
from core.models import NewsItem, CachedNewsItem
from django.utils import timezone
from news_aggregator.settings import DEFAULT_EXPIRATION_TIME


class DatabaseCacheManager(CacheManager):
    """
    A cache manager that stores news items in a database and retrieves them from cache if they have been fetched
    within the expiration time.

    Attributes:
        expiration_time (int): The number of seconds that the news items can be stored in cache before they expire.
    """

    def __init__(self, expiration_time=DEFAULT_EXPIRATION_TIME):
        """
        Initializes the `DatabaseCacheManager` object.

        Args:
            expiration_time (int, optional): The number of seconds that the news items can be stored in cache before
                they expire. Defaults to the `DEFAULT_EXPIRATION_TIME` value from the settings.
        """
        self.expiration_time = expiration_time
        
    def fetch(self, query=None) -> List[NewsItem]:
        """
        Fetches news items from cache if they exist and have not expired, otherwise returns None.

        Args:
            query (str, optional): The search query for the news items. Defaults to None.

        Returns:
            A list of news items from cache if they exist and have not expired, otherwise None.
        """
        cache = CachedNewsItem.objects.filter(query=query, last_fetched__gte=timezone.now()-timedelta(seconds=self.expiration_time))
        news_items = [item.news_item for item in cache]
        if cache.exists():
            cache.update(last_fetched=timezone.now())
            return news_items
        else:
            return None
    
    def store(self, news_items, query=None) -> List[NewsItem]:
        """
        Stores news items in cache and returns the stored news items.

        Args:
            news_items (list[NewsItem]): A list of news items to store in cache.
            query (str, optional): The search query for the news items. Defaults to None.

        Returns:
            A list of stored news items.
        """
        result = []
        with transaction.atomic():
            for news_item in news_items:
                updated_news_item, created = NewsItem.objects.get_or_create(headline=news_item.headline, link=news_item.link, source=news_item.source)
                result.append(updated_news_item)
            CachedNewsItem.objects.filter(query=query).delete()
            CachedNewsItem.objects.bulk_create([CachedNewsItem(news_item=item, query=query, last_fetched=timezone.now()) for item in result])
        return result

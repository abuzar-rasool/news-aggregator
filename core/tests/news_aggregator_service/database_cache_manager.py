from datetime import timedelta
from django.test import TestCase
from django.utils import timezone

from core.models import NewsItem, CachedNewsItem
from core.news_aggregator_service.cache_manager import DatabaseCacheManager, CacheManager


class TestDatabaseCacheManager(TestCase):
    def setUp(self):
        self.expiration_time = 10
        self.cache_manager = DatabaseCacheManager(expiration_time=self.expiration_time)
        self.sample_news_items = [
            NewsItem(headline='News 1', link='https://example.com/news1', source='Example Source'),
            NewsItem(headline='News 2', link='https://example.com/news2', source='Example Source'),
        ]

    def test_fetch(self):
        # Test fetching from empty cache
        result = self.cache_manager.fetch()
        self.assertIsNone(result)

        # Store sample news items in the cache
        self.cache_manager.store(self.sample_news_items)

        # Test fetching stored news items
        result = self.cache_manager.fetch()
        self.assertEqual(len(result), len(self.sample_news_items))

        # Test fetching expired news items
        CachedNewsItem.objects.update(last_fetched=timezone.now() - timedelta(seconds=self.expiration_time + 1))
        result = self.cache_manager.fetch()
        self.assertIsNone(result)

    def test_store(self):
        # Test storing news items
        stored_news_items = self.cache_manager.store(self.sample_news_items)
        self.assertEqual(len(stored_news_items), len(self.sample_news_items))

        # Test if news items are saved in the cache
        cached_news_items = CachedNewsItem.objects.all()
        self.assertEqual(len(cached_news_items), len(self.sample_news_items))

        # Test storing duplicate news items
        duplicate_news_items = [
            NewsItem(headline='News 1', link='https://example.com/news1', source='Example Source'),
            NewsItem(headline='News 3', link='https://example.com/news3', source='Example Source'),
        ]

        stored_news_items = self.cache_manager.store(duplicate_news_items)
        self.assertEqual(len(stored_news_items), len(duplicate_news_items))

        # Test if duplicate news items are not stored again in the database
        news_items = NewsItem.objects.all()
        self.assertEqual(len(news_items), len(self.sample_news_items) + 1)  # Only one new news item

        # Test if the cache is updated with the new news items
        cached_news_items = CachedNewsItem.objects.all()
        self.assertEqual(len(cached_news_items), len(duplicate_news_items))

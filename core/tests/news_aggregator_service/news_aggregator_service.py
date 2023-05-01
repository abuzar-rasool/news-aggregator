import unittest
from unittest.mock import MagicMock
from core.news_aggregator_service import NewsAggregatorService, NewsFetcher, CacheManager
from core.models import NewsItem

class MockNewsFetcher(NewsFetcher):
    def fetch_data(self, query=None):
        return [NewsItem(headline='Mock News', link='https://example.com/mock-news', source='mock')]

class MockCacheManager(CacheManager):
    def fetch(self, query=None):
        return None

    def store(self, news_data, query=None):
        return news_data

class TestNewsAggregatorService(unittest.TestCase):
    def setUp(self):
        self.news_fetchers = [MockNewsFetcher()]
        self.cache_manager = MockCacheManager()
        self.service = NewsAggregatorService(self.news_fetchers, self.cache_manager)

    def test_fetch_combined_news_data(self):
        # Test fetching data with empty cache
        combined_data = self.service.fetch_combined_news_data()
        self.assertEqual(len(combined_data), len(self.news_fetchers))

        # Test fetching data with non-empty cache
        self.cache_manager.fetch = MagicMock(return_value=[NewsItem(headline='Cached News', link='https://example.com/cached-news', source='cached')])
        combined_data = self.service.fetch_combined_news_data()
        self.assertEqual(len(combined_data), 1)
        self.cache_manager.fetch.assert_called()

        # Test fetching data with a query
        query = 'example query'
        combined_data = self.service.fetch_combined_news_data(query)
        self.assertEqual(len(combined_data), 1)
        self.cache_manager.fetch.assert_called_with(query)

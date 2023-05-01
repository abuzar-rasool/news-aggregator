import unittest
from unittest.mock import MagicMock
from core.news_aggregator_service.news_fetcher import NewsAPIFetcher, RedditFetcher
from core.models import NewsItem



class TestNewsAPIFetcherService(unittest.TestCase):
    def setUp(self):
        self.fetcher = NewsAPIFetcher()

    def test_service_up(self):
        try:
            news_items = self.fetcher.fetch_data()
            self.assertIsInstance(news_items, list)
            self.assertIsInstance(news_items[0], NewsItem)
        except Exception as e:
            self.fail(f"NewsAPIFetcher service is down: {e}")

class TestRedditFetcherService(unittest.TestCase):
    def setUp(self):
        self.fetcher = RedditFetcher()

    def test_service_up(self):
        try:
            news_items = self.fetcher.fetch_data()
            self.assertIsInstance(news_items, list)
            self.assertIsInstance(news_items[0], NewsItem)
        except Exception as e:
            self.fail(f"RedditFetcher service is down: {e}")

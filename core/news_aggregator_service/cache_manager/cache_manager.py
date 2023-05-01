from abc import ABC, abstractmethod
from core.models import NewsItem

class CacheManager(ABC):
    """
    Abstract base class for cache managers that fetch and store news items.
    """
    @abstractmethod
    def fetch(self, query=None) -> list[NewsItem]:
        """
        Fetches news items from the cache.

        :param query: The search query string.
        :return: A list of NewsItem objects.
        """
        pass

    @abstractmethod
    def store(self, news_data, query=None) -> list[NewsItem]:
        """
        Stores news items in the cache.

        :param news_data: A list of NewsItem objects.
        :param query: The search query string.
        :return: A list of NewsItem objects.
        """
        pass

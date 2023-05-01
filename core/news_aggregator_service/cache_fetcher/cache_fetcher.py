from abc import ABC, abstractmethod
from core.models import NewsItem

class CacheFetcher(ABC):
    @abstractmethod
    def fetch(self, query=None) -> list[NewsItem]:
        pass

    @abstractmethod
    def store(self, news_data, query=None) -> list[NewsItem]:
        pass
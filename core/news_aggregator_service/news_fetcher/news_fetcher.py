from abc import ABC, abstractmethod
from core.models import NewsItem
from news_aggregator.config import DEFAULT_PAGE_SIZE

class NewsFetcher(ABC):
    def __init__(self, limit=DEFAULT_PAGE_SIZE):
        self.limit = limit
    
    @abstractmethod
    def fetch_data(self, query:str=None) -> list[NewsItem]:
        pass
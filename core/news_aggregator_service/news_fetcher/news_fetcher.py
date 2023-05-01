from abc import ABC, abstractmethod
from core.models import NewsItem

DEFAULT_PAGE_SIZE = 2

class NewsFetcher(ABC):
    def __init__(self, limit=DEFAULT_PAGE_SIZE):
        self.limit = limit
    
    @abstractmethod
    def fetch_data(self, query:str=None) -> list[NewsItem]:
        pass
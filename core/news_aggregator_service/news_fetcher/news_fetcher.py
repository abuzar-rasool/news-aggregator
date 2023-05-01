from abc import ABC, abstractmethod
from core.models import NewsItem
from news_aggregator.config import DEFAULT_PAGE_SIZE


class NewsFetcher(ABC):
    """
    Abstract inteface for implementing fecthers class for fetching news data from a source.
    """
    
    def __init__(self, limit=DEFAULT_PAGE_SIZE):
        """
        Constructor method for NewsFetcher.
        
        :param limit: Maximum number of news items to fetch in one request. Default is 2.
        """
        self.limit = limit
    
    @abstractmethod
    def fetch_data(self, query:str=None) -> list[NewsItem]:
        """
        Abstract method for fetching news data from a source.
        
        :param query: Optional query parameter for filtering news items based on a keyword.
        :return: A list of NewsItem objects fetched from the source.
        """
        pass

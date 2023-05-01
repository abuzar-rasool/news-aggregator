from .news_fetcher import *
from .cache_manager import *
from .exceptions import FailedToRetriveData

class NewsAggregatorService:
    def __init__(self, news_fetchers: list[NewsFetcher], cache_manager: CacheManager):
        self.news_fetchers = news_fetchers
        self.cache_fetcher = cache_manager

    def fetch_combined_news_data(self,query:str=None):
        # First, try to fetch news data from the cache
        cached_data = self.cache_fetcher.fetch(query)

        if cached_data:
            return cached_data

        # If the cache is empty or expired, fetch news data from external sources
        combined_data = []
        for fetcher in self.news_fetchers:  
            news_data = fetcher.fetch_data(query)
            combined_data.extend(news_data)
            


        # Store the fetched data in the cache
        combined_data = self.cache_fetcher.store(combined_data, query)

        return combined_data
    

news_aggregator_service = NewsAggregatorService([RedditFetcher(), NewsAPIFetcher()], DatabaseCacheManager())
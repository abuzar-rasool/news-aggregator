from .news_fetcher import *
from newsapi import NewsApiClient
from news_aggregator.config import NEWS_API_KEY


class NewsAPIFetcher(NewsFetcher):
    """
    A class for fetching news data from News API.
    
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the NewsAPIFetcher object.
        """
        self.newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        super().__init__()

    def fetch_data(self, query=None):
        """
        Fetches news data from News API.

        Parameters
        ----------
        query : str, optional
            A query term to search for in the news.

        Returns
        -------
        List[NewsItem]
            A list of NewsItem objects representing the fetched news data.
        """
        if query:
            results = self.newsapi.get_everything(q=query, language='en', page_size=self.limit)
        else:
            results = self.newsapi.get_top_headlines(language='en', page_size=self.limit)

        data = []

        for article in results['articles']:
            item = NewsItem(headline=article['title'], link=article['url'], source='newsapi')
            data.append(item)

        return data

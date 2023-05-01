from .news_fetcher import *
from newsapi import NewsApiClient

NEWS_API_KEY = '052201da5fbb4ec5a36d55c94c65013c'

class NewsAPIFetcher(NewsFetcher):
    
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        super().__init__()
    
    def fetch_data(self, query=None):
        if query:
            results = self.newsapi.get_everything(q=query, language='en', page_size=self.limit)
        else:
            results = self.newsapi.get_top_headlines(language='en', page_size=self.limit)

        data = []
        
        for article in results['articles']:
            item = NewsItem(headline=article['title'], link=article['url'], source='newsapi')
            data.append(item)
        
        return data
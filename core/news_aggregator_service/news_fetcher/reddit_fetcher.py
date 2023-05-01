from .news_fetcher import *
import praw
from news_aggregator.settings import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT


class RedditFetcher(NewsFetcher):
    def __init__(self):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

        super().__init__()
    
    def fetch_data(self, query=None):
        subreddit = self.reddit.subreddit('news')
        if query:
            results = subreddit.search(query, limit=self.limit)
        else:
            results = subreddit.hot(limit=self.limit)

        data = []
        for post in results:
            item = NewsItem(headline=post.title, link=post.url, source='reddit')
            data.append(item)
        return data
import praw
import requests
from newsapi import NewsApiClient

REDDIT_CLIENT_ID = 'ziZLXRqA1S8LM22s_8rS6g'
REDDIT_SECRET = 'asFaNLoptook3_DA6b13QSKDHpaNPA'
REDDIT_USER_AGENT = 'by u/Grand-Cauliflower-33'
NEWS_API_KEY = 'your_news_api_key'
DEFAULT_PAGE_SIZE = 5

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_reddit_data(query=None):
    subreddit = reddit.subreddit('news')
    if query:
        results = subreddit.search(query, limit=DEFAULT_PAGE_SIZE)
    else:
        results = subreddit.hot(limit=10)

    data = []
    for post in results:
        print(post.id)
        item = {
            'headline': post.title,
            'link': post.url,
            'source': 'reddit',
        }
        data.append(item)

    return data

def fetch_news_api_data(query=None):
    if query:
        results = newsapi.get_everything(q=query, language='en', page_size=DEFAULT_PAGE_SIZE)
    else:
        results = newsapi.get_top_headlines(language='en', page_size=DEFAULT_PAGE_SIZE)

    data = []
    for article in results['articles']:
        item = {
            'headline': article['title'],
            'link': article['url'],
            'source': 'newsapi',
        }
        data.append(item)

    return data
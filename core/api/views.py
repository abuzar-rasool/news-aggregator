from core.news_aggregator import news_aggregator
from .serializers import NewsItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_news(request, format=None):
    news = news_aggregator.fetch_combined_news_data()
    serializer = NewsItemSerializer(news, many=True)
    return Response(serializer.data)
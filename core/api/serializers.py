from rest_framework import serializers
from core.models import NewsItem, Favourite

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'headline', 'link', 'source']

class GetFavouriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='news_item.id')
    headline = serializers.CharField(source='news_item.headline')
    link = serializers.CharField(source='news_item.link')
    source = serializers.CharField(source='news_item.source')

    class Meta:
        model = Favourite
        fields = ['id', 'headline', 'link', 'source']

class PostFavouriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='news_item.id')
    headline = serializers.CharField(source='news_item.headline')
    link = serializers.CharField(source='news_item.link')
    source = serializers.CharField(source='news_item.source')
    
    class Meta:
        model = Favourite
        fields = ['id', 'headline', 'link', 'source', 'is_favourite']

# dummy serializers for swagger
class CustomBaseExceptionSerializer(serializers.Serializer):
    error = serializers.CharField()

class UnauthenticatedErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
    
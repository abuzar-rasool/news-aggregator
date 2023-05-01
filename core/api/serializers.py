from rest_framework import serializers
from core.models import NewsItem

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'headline', 'link', 'source']
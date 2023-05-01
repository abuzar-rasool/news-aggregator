from core.news_aggregator import news_aggregator
from .serializers import NewsItemSerializer, FavouriteSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import NewsItem
from core.models import Favourite
from rest_framework import generics

@extend_schema(
        responses=NewsItemSerializer,
        parameters=[
            OpenApiParameter(name='query', description='Search Query', type=str),
        ],
    )
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_news(request):
    query = request.query_params.get('query', None)
    news = news_aggregator.fetch_combined_news_data(query)
    serializer = NewsItemSerializer(news, many=True)
    return Response(serializer.data)




class FavouriteAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=NewsItemSerializer,
        parameters=[
            OpenApiParameter(name='user', description='User Name', type=str),
            OpenApiParameter(name='id', description='News Id', type=str),
        ],
    )
    def post(self, request, *args, **kwargs):
        news_id = request.query_params.get('id', None)
        user_name = request.query_params.get('user', None)
        
        if not user_name:
            return Response({'message': 'User name is required'}, status=400)
        
        if not news_id:
            return Response({'message': 'News id is required'}, status=400)
        
        try:
            news_item = NewsItem.objects.get(pk=news_id)
        except NewsItem.DoesNotExist:
            return Response({'message': 'News item not found'}, status=400)

        user, _ = User.objects.get_or_create(username=user_name)

        favourite, created = Favourite.objects.get_or_create(user=user, news_item=news_item)
        
        if not created:
            favourite.delete()

            

        favourites = Favourite.objects.filter(user=user).order_by('-created_at')
        
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        responses=NewsItemSerializer,
        parameters=[
            OpenApiParameter(name='user', description='User Name', type=str),
        ],
    )
    def get(self, request, *args, **kwargs):
    
        user_name = request.query_params.get('user', None)
        if not user_name:
            return Response({'message': 'User name is required'}, status=400)
        try:
            user= User.objects.get(username=user_name)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=400)
        

        favourites = Favourite.objects.filter(user=user).order_by('-created_at')
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data)



class BaseException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class UserRequiredException(BaseException):
    def __init__(self):
        super().__init__('User name is required', 400)

class NewsItemRequiredException(BaseException):
    def __init__(self):
        super().__init__('News id is required', 400)

class NewsItemNotFoundException(BaseException):
    def __init__(self):
        super().__init__('News item not found', 400)

class UserNotFoundException(BaseException):
    def __init__(self):
        super().__init__('User not found', 400)



class FavouriteService():
    def get_favourites(self, user) -> list[Favourite]:
        
        if not user:
            raise UserRequiredException()
        try:
            user= User.objects.get(username=user)
        except User.DoesNotExist:
            raise UserNotFoundException()
        
        favourites = list(Favourite.objects.filter(user=user).order_by('-created_at'))
        return favourites
    
    

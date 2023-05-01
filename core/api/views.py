"""
This module contains two API views for News and Favourites management. Both views are
protected by authentication.

Dependencies:
- serializers: NewsItemSerializer, FavouriteSerializer
- rest_framework classes: Response, extend_schema, OpenApiParameter, extend_schema_view,
  api_view, permission_classes, IsAuthenticated, generics
- custom_base_exception: CustomBaseException
- services: news_aggregator_service, favourite_service
"""

from .serializers import NewsItemSerializer, FavouriteSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from core.custom_base_exception import CustomBaseException

from core.news_aggregator_service import news_aggregator_service
from core.favourite_service.favourite_service import favourite_service


class NewsAPIView(generics.GenericAPIView):
    """
    NewsAPIView is a generic API view that handles fetching news data based on a given query.
    
    Permissions:
    - IsAuthenticated: Ensures that only authenticated users can access this view.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=NewsItemSerializer,
        parameters=[
            OpenApiParameter(name='query', description='Search Query', type=str),
        ],
    )
    def get(self, request, *args, **kwargs):
        """
        Fetches news data based on the given query and returns the serialized response.
        The data is fetched from news_aggregator_service which is responsible for fetching
        and caching news data from external sources.

        """
        try:
            query = request.query_params.get('query', None)
            news = news_aggregator_service.fetch_combined_news_data(query)
            serializer = NewsItemSerializer(news, many=True)
            return Response(serializer.data)
        except CustomBaseException as e:
            return Response(e.message, status=e.status_code)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=500)


@extend_schema_view(
    post=extend_schema(
        responses=FavouriteSerializer,
        parameters=[
            OpenApiParameter(name='user', description='User Name', type=str),
            OpenApiParameter(name='id', description='News Id', type=str),
        ],
    ),
    get=extend_schema(
        responses=FavouriteSerializer,
        parameters=[
            OpenApiParameter(name='user', description='User Name', type=str),
        ],
    )
)
class FavouriteAPIView(generics.ListAPIView):
    """
    FavouriteAPIView is a generic List API view that handles managing user's favourite news.
    
    Permissions:
    - IsAuthenticated: Ensures that only authenticated users can access this view.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        """
        Toggles a news item as favourite for the given user and returns the updated favourites list.
        
        """
        try:
            favourites = favourite_service.toggle_favourite(request.query_params.get('user', None), request.query_params.get('id', None))
            serializer = FavouriteSerializer(favourites, many=True)
            return Response(serializer.data)
        except CustomBaseException as e:
            return Response({'message': e.message}, status=e.status_code)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=500)
    

    def get(self, request, *args, **kwargs):
        """
        Fetches the favourite news list for the given user and returns the serialized response.
        
        """
        try:
            favourites = favourite_service.get_favourites(request.query_params.get('user', None))
            serializer = FavouriteSerializer(favourites, many=True)
            return Response(serializer.data)
        except CustomBaseException as e:
            return Response({'message': e.message}, status=e.status_code)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=500)
    



from .serializers import NewsItemSerializer, FavouriteSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from core.custom_base_exception import CustomBaseException
# services
from core.news_aggregator_service import news_aggregator_service
from core.favourite_service.favourite_service import favourite_service


class NewsAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=NewsItemSerializer,
        parameters=[
            OpenApiParameter(name='query', description='Search Query', type=str),
        ],
    )
    def get(self, request, *args, **kwargs):
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
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            favourites = favourite_service.toggle_favourite(request.query_params.get('user', None), request.query_params.get('id', None))
            serializer = FavouriteSerializer(favourites, many=True)
            return Response(serializer.data)
        except CustomBaseException as e:
            return Response({'message': e.message}, status=e.status_code)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=500)
    

    
    def get(self, request, *args, **kwargs):
        try:
            favourites = favourite_service.get_favourites(request.query_params.get('user', None))
            serializer = FavouriteSerializer(favourites, many=True)
            return Response(serializer.data)
        except CustomBaseException as e:
            return Response({'message': e.message}, status=e.status_code)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=500)
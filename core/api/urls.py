from django.contrib import admin
from django.urls import path, re_path
from .views import get_news
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import get_news, FavouriteAPIView




urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('news/',get_news,name='get_news'),
    path('news/favourite', FavouriteAPIView.as_view(), name='favourite_news'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

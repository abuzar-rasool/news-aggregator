from django.contrib import admin
from django.urls import path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import NewsAPIView, FavouriteAPIView




urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('news/',NewsAPIView.as_view(),name='get_news'),
    path('news/favourite', FavouriteAPIView.as_view(), name='favourite_news'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

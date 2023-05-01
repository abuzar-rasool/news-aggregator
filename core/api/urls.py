from django.contrib import admin
from django.urls import path,include
from .views import get_news

urlpatterns = [
    path('',get_news,name='get_news'),
]

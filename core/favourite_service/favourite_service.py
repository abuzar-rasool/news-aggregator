from django.contrib.auth.models import User
from core.models import Favourite, NewsItem
from .exceptions import UserRequiredException, UserNotFoundException, NewsItemRequiredException, NewsItemNotFoundException



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
    
    def toggle_favourite(self, user, id) -> list[Favourite]:
        news_id = id
        user_name = user
        
        if not user_name:
            raise UserRequiredException()
        
        if not news_id:
            raise NewsItemRequiredException()
        
        try:
            news_item = NewsItem.objects.get(pk=news_id)
        except NewsItem.DoesNotExist:
            raise NewsItemNotFoundException()

        user, _ = User.objects.get_or_create(username=user_name)

        favourite, created = Favourite.objects.get_or_create(user=user, news_item=news_item)
        
        if not created:
            favourite.delete()

        return self.get_favourites(user)
    
favourite_service = FavouriteService()
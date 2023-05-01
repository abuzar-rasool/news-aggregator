from django.contrib.auth.models import User
from core.models import Favourite, NewsItem
from .exceptions import UserRequiredException, UserNotFoundException, NewsItemRequiredException, NewsItemNotFoundException

class FavouriteService():
    """
    Service class for managing user's favourite news items.
    """
    
    def get_favourites(self, user) -> list[Favourite]:
        """
        Returns a list of user's favourite news items in descending order of creation. If the user is not found, it will raise an exception.
        
        
        :param user: The username of the user whose favourites need to be retrieved.
        :raises UserRequiredException: If no user is provided.
        :raises UserNotFoundException: If user with the provided username is not found.
        :return: List of user's favourite news items.
        """
        if not user:
            raise UserRequiredException()
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            raise UserNotFoundException()
        
        favourites = list(Favourite.objects.filter(user=user, is_favourite=True).order_by('-created_at'))
        return favourites
    
    def toggle_favourite(self, user, id) -> list[Favourite]:
        """
        Toggles the favourite status of a news item for a user. If the news item is already a favourite, it will be removed from the user's favourites.
        If the news item is not a favourite, it will be added to the user's favourites. If the user is not found, it will be created.
        
        :param user: The username of the user.
        :param id: The id of the news item to toggle favourite.
        :raises UserRequiredException: If no user is provided.
        :raises NewsItemRequiredException: If no news item id is provided.
        :raises NewsItemNotFoundException: If no news item with the provided id is found.
        :return: List of user's favourite news items.
        """
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
            favourite.is_favourite = not favourite.is_favourite
            favourite.save()
        
        favourites = list(Favourite.objects.filter(user=user).order_by('-created_at'))
        return favourites
    
favourite_service = FavouriteService()

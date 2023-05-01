from django.test import TestCase
from django.contrib.auth.models import User
from core.models import NewsItem, Favourite
from core.favourite_service import FavouriteService, UserRequiredException, NewsItemRequiredException, NewsItemNotFoundException, UserNotFoundException

class TestFavouriteService(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.news_item = NewsItem.objects.create(headline='Test News', link='https://example.com/test-news', source='test')
        self.service = FavouriteService()

    def test_get_favourites(self):
        # Test with a non-existent user
        with self.assertRaises(UserNotFoundException):
            self.service.get_favourites('nonexistentuser')

        # Test with a valid user
        favourites = self.service.get_favourites(self.user.username)
        self.assertEqual(len(favourites), 0)

    def test_toggle_favourite(self):
        # Test with no user
        with self.assertRaises(UserRequiredException):
            self.service.toggle_favourite(None, self.news_item.id)

        # Test with no news item
        with self.assertRaises(NewsItemRequiredException):
            self.service.toggle_favourite(self.user.username, None)

        # Test with a non-existent news item
        with self.assertRaises(NewsItemNotFoundException):
            self.service.toggle_favourite(self.user.username, -1)

        # Test adding a favourite
        favourites = self.service.toggle_favourite(self.user.username, self.news_item.id)
        self.assertEqual(len(favourites), 1)
        self.assertEqual(favourites[0].news_item, self.news_item)

        # Test removing a favourite
        favourites = self.service.toggle_favourite(self.user.username, self.news_item.id)
        self.assertEqual(len(favourites), 1)
        self.assertEqual(favourites[0].is_favourite, False)

import allure
import pytest
import time
from config.base_test import BaseTest



@allure.epic("Administration")
@allure.feature("Wishlist")
class TestWishlist(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Getting User's wishlist")
    def test_user_wishlist(self):
        self.api_wishlist.get_user_wishlist()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Adding game to User's wishlist")
    def test_add_game_to_user_wishlist(self):
        game_uuid = self.api_games.random_game_uuid()
        uuid = self.api_users.get_random_user_id()
        self.api_wishlist.add_game_to_user_wishlist(game_uuid, uuid)

    @pytest.mark.critical_path
    @pytest.mark.regress
    @allure.title("Removing game from User's wishlist")
    def test_remove_game_from_user_wishlist(self):
        game_uuid = self.api_games.random_game_uuid()
        uuid = self.api_users.get_random_user_id()
        self.api_wishlist.add_game_to_user_wishlist(game_uuid, uuid)
        print(f"✅ Game {game_uuid} added to wishlist for user {uuid}")
        self.api_wishlist.remove_game_from_user_wishlist(game_uuid, uuid)
        print(f"❌ Game {game_uuid} removed from wishlist for user {uuid}")


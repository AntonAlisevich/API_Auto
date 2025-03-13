import allure
import pytest

from config.base_test import BaseTest



@allure.epic("Administration")
@allure.feature("Games")
class TestGames(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Get full list of games")
    def test_get_full_list_of_games(self):
        self.api_games.get_list_of_games()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Get one game by title")
    def test_get_game(self):
        games = self.api_games.search_games()
        self.api_games.get_game_by_title(games, self.api_games.random_game_title())

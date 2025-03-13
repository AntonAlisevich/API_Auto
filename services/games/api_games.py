import requests
import allure
import  random
from utils.helper import Helper
from services.games.endpoints import Endpoints
from config.headers import Headers
from services.games.models.games_model import GamesModel


class GamesAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get full list of games")
    def get_list_of_games(self):
        response = requests.get(
            url=self.endpoints.get_games,
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GamesModel.GamesListModel(**response.json())
        return model

    @allure.step("Search games")
    def search_games(self):
        response = requests.get(
            url=self.endpoints.get_games_search,
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        return response.json()["games"]

    @allure.step("Select random game uuid from the list")
    def random_game_uuid(self):
        list_of_uuids = self.search_games()
        random_uuid = random.choice([game["uuid"] for game in list_of_uuids])
        return random_uuid

    @allure.step("Select random game by title from the list")
    def random_game_title(self):
        list_of_games = self.search_games()
        random_title = random.choice([game["title"] for game in list_of_games])
        return random_title

    @allure.step("Get game")
    def get_game_by_title(self, games, title):
        for game in games:
            if game["title"].lower() == title.lower():
                uuid = game["uuid"]
                response = requests.get(
                    url=self.endpoints.get_game(uuid),
                    headers=self.headers.basic,
                )
                assert response.status_code == 200, response.json()
                self.attach_response(response.json())
                model = GamesModel.GameModel(**response.json())
                return model


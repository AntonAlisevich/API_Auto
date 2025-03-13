import requests
import allure
from utils.helper import Helper
from services.wishlists.payloads import Payloads
from services.wishlists.endpoints import Endpoints
from config.headers import Headers
from services.wishlists.models.wishlist_model import WishlistModel
from services.users.api_users import UsersAPI


class WhishlistAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get user's wishlist")
    def get_user_wishlist(self):
        users_api = UsersAPI()
        users_list = users_api.get_all_users()

        if users_list["users"]:
            uuid = users_api.get_random_user_id()
        else:
            users_api.delete_all_users()
            user = users_api.create_user()
            uuid = user.uuid

        response = requests.get(
            url=self.endpoints.get_wishlist(uuid),
            headers=self.headers.basic,
        )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = WishlistModel.UserWishlistModel(**response.json())
        return model

    @allure.step("Add game to user's wishlist")
    def add_game_to_user_wishlist(self, game_uuid, uuid):
        response = requests.post(
            url=self.endpoints.add_to_user_wishlist(uuid),
            headers=self.headers.basic,
            json=self.payloads.add_to_wishlist(game_uuid)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = WishlistModel.UserWishlistModel(**response.json())
        return model

    @allure.step("Remove game from user's wishlist")
    def remove_game_from_user_wishlist(self, game_uuid, uuid):
        response = requests.post(
            url=self.endpoints.remove_from_user_wishlist(uuid),
            headers=self.headers.basic,
            json=self.payloads.remove_from_wishlist(game_uuid)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = WishlistModel.UserWishlistModel(**response.json())
        return model

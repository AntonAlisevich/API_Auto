import requests
import allure
import random
from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from config.headers import Headers
from services.users.models.user_model import UserModel
from services.users.endpoints import HOST


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get all users")
    def get_all_users(self):
        response = requests.get(
            url=self.endpoints.get_users,
            headers=self.headers.basic,
            params={"limit": 20},
        )
        assert response.status_code == 200, response.json()
        return response.json()

    @allure.step("Get random user uuid")
    def get_random_user_id(self):
        users_list = self.get_all_users()
        users = users_list["users"]
        list_uuids = []
        for user in users:
            list_uuids.append(user["uuid"])
        random_id = random.choice(list_uuids)
        return random_id

    @allure.step("Delete user by ID")
    def delete_user(self, uuid):
        response = requests.delete(
            url=self.endpoints.delete_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 204, response.json()

    @allure.step("Update user by ID")
    def update_user_by_id(self, uuid):
        response = requests.patch(
            url=self.endpoints.update_user_by_id(uuid),
            headers=self.headers.basic,
            json=self.payloads.update_user,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Login user by login and password")
    def login_user_with_creds(self):
        response = requests.post(
            url=self.endpoints.login_user,
            headers=self.headers.basic,
            json=self.payloads.login_payload(),
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Delete all users")
    def delete_all_users(self):
        feature = self.get_all_users()
        data = feature["users"]
        for i in data:
            response = requests.delete(
                url=f"{HOST}/users/{i['uuid']}",
                headers=self.headers.basic,
            )
            assert response.status_code == 204, response.json()

    def create_20_users(self):
        users = []  # собираем всех юзеров в список
        for _ in range(1, 21):
            json = self.payloads.create_users()  # динамический payload
            response = requests.post(
                url=self.endpoints.create_user,
                headers=self.headers.basic,
                json=json,
            )
            assert response.status_code == 200, response.json()
            self.attach_response(response.json())
            model = UserModel(**response.json())
            users.append(model)
        return users

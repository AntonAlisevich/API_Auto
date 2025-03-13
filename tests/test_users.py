import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.fixture(autouse=True)
    def cleanup_users(self):
        """Очищаем список юзеров перед каждым тестом"""
        self.api_users.delete_all_users()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)
        self.api_users.delete_user(user.uuid)

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Delete created user")
    def test_delete_user(self):
        user = self.api_users.create_user()
        self.api_users.delete_user(user.uuid)

    @pytest.mark.critical_path
    @pytest.mark.regress
    @allure.title("Update created user")
    def test_update_user(self):
        user = self.api_users.create_user()
        self.api_users.update_user_by_id(user.uuid)
        self.api_users.delete_user(user.uuid)

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title("Login under created user")
    def test_login_user(self):
        user = self.api_users.create_user()
        self.api_users.login_user_with_creds()
        self.api_users.delete_user(user.uuid)

    @pytest.mark.regress
    @pytest.mark.critical_path
    @allure.title("Create full list of users")
    def test_delete_users(self):
        self.api_users.create_20_users()



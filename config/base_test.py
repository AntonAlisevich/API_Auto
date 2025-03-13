from services.users.api_users import UsersAPI
from services.games.api_games import GamesAPI
from services.wishlists.api_wishlist import WhishlistAPI


class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_games = GamesAPI()
        self.api_wishlist = WhishlistAPI()



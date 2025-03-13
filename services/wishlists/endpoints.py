import os

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" \
    else "https://release-gs.qa-playground.com/api/v1"


class Endpoints:

    get_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist"
    add_to_user_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/add"
    remove_from_user_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/remove"


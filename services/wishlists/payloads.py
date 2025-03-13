
class Payloads:

    @staticmethod
    def add_to_wishlist(game_uuid):
        return {"item_uuid": game_uuid}

    @staticmethod
    def remove_from_wishlist(game_uuid):
        return {"item_uuid": game_uuid}


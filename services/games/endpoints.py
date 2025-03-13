import os

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" \
    else "https://release-gs.qa-playground.com/api/v1"


class Endpoints:

    get_games = f"{HOST}/games"
    get_games_search = f"{HOST}/games/search"
    get_game = lambda self, uuid: f"{HOST}/games/{uuid}"


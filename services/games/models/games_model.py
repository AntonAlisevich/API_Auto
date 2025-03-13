from pydantic import BaseModel, field_validator


class GamesModel:

    class GamesListModel(BaseModel):
        games: list
        meta: dict

        @field_validator("games", "meta")
        def fields_for_list_of_games_are_not_empty(cls, value):
            if value == "" or value is None:
                raise ValueError("Field is empty")
            else:
                return value

    class GameModel(BaseModel):
        category_uuids: list
        uuid: str
        price: int
        title: str

        @field_validator("category_uuids", "price", "title", "uuid")
        def fields_are_not_empty(cls, value):
            if value == "" or value is None:
                raise ValueError("Field is empty")
            else:
                return value



from pydantic import BaseModel, field_validator


class WishlistModel:

    class UserWishlistModel(BaseModel):
        items: list
        user_uuid: str

        @field_validator("items", "user_uuid")
        def fields_for_user_wishlist_are_not_empty(cls, value):
            if value == "" or value is None:
                raise ValueError("Field is empty")
            else:
                return value

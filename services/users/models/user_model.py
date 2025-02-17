from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    uuid: str
    name: str
    nickname: str

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

# response = {
#         "email": "max@gmail.com",
#         "password": "password",
#         "name": "Max",
#         "nickname": "max"
#     }
#
# user = UserModel(**response)
# print(user.nickname)
# print(user.name)

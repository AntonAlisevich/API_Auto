from faker import Faker

fake = Faker()


class Payloads:
    @staticmethod
    def create_users():
        return {
            "email": fake.email(),
            "password": fake.password(length=8),
            "name": fake.first_name(),
            "nickname": fake.user_name()
        }

    create_user = {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    update_user = {
        "email": fake.email(),
        "password": fake.password(length=12),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    def login_payload(self):
        login = self.create_user
        log_creds = {}
        for i in range(1):
            log_creds["email"] = login["email"]
            log_creds["password"] = login["password"]
        return log_creds


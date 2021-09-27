from api.Repositories.Documents.user import User
from api.Repositories.db import DataBase


class UserRepository(DataBase):
    def __init__(self):
       super().__init__()

    def add_user(self, data):
        user = User(name = data.name).save()
        return user
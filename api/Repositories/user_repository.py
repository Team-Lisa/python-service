from api.models.user import User
from api.Repositories.db import DataBase


class UserRepository(DataBase):
    def __init__(self):
       super().__init__()

    def add_user(self, user):
        return user.save()


    def get_user_by_name(self,value):
        user = User.objects(name=value)
        return user

    def delete_all_users(self):
        User.objects().delete()

    def get_all_users(self):
        return User.objects()
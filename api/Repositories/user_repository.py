from api.models.user import User
from api.Repositories.db import DataBase


class UserRepository():

    @staticmethod
    def add_user(user):
        return user.save()

    @staticmethod
    def get_user_by_name(value):
        user = User.objects(name=value)
        return user

    @staticmethod
    def delete_all_users():
        User.objects().delete()

    @staticmethod
    def get_all_users():
        return User.objects()
from api.Repositories.user_repository import UserRepository
from api.models.user import User
from fastapi import HTTPException
import json


class UserController:

    @staticmethod
    def create(user):
        user = User(name = user.name)
        result = UserRepository().add_user(user)
        return {"user": result.to_json()}


    @staticmethod
    def find_by_name(name):
        raise HTTPException(status_code=404, detail="User not found")
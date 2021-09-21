from api.models.user import User
from fastapi import HTTPException


class UserController:

    @staticmethod
    def create(user):
        user = User(user.name)
        # save user
        return {"user": user.json()}


    @staticmethod
    def find_by_name(name):
        raise HTTPException(status_code=404, detail="User not found")
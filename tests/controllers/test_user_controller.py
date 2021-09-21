import pytest

from api.controllers.user_controller import UserController
from api.models.requests.user import User
from fastapi import HTTPException


def test_response():
    name = "mockname"
    user = User(name=name)
    response = UserController.create(user)
    assert response == {
        "user": {
            "name": name
        }
    }


def test_user_not_found():
    name = "mockname"

    with pytest.raises(HTTPException) as e_info:
        UserController.find_by_name(name)

from fastapi import APIRouter
from api.models.requests.user import User
from api.controllers.user_controller import UserController
from api.models.responses.user import User as UserResponse

router = APIRouter(tags=["Users"])


@router.post("/users", response_model=UserResponse)
async def create_user(user: User):
    return UserController.create(user)


@router.get("/users")
async def find_user(name: str = ""):
    return UserController.find_by_name(name)



from api.Repositories.user_repository import UserRepository
from api.models.user import User


def test_add_user_successfully():
    repo = UserRepository()
    result = repo.add_user(User(name = "nick"))
    assert result.name == "nick"
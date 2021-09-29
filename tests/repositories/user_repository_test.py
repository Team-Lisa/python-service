from api.Repositories.user_repository import UserRepository
from api.models.user import User


def test_add_user_successfully(init):
    repo = UserRepository()
    result = repo.add_user(User(name = "nick"))
    assert result.name == "nick"

def test_get_user_by_name_successfully(init):
    repo = UserRepository()
    name = "nick"
    repo.add_user(User(name=name))
    result = repo.get_user_by_name(name)
    assert result[0].name == "nick"


def test_delete_all_users(init):
    repo = UserRepository()
    repo.delete_all_users()
    result = repo.get_all_users()
    assert result.count() == 0

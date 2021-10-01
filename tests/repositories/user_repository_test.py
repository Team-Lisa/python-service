from api.Repositories.user_repository import UserRepository
from api.models.user import User


def test_add_user_successfully(init):
    result = UserRepository.add_user(User(name = "nick"))
    assert result.name == "nick"

def test_get_user_by_name_successfully(init):
    name = "nick"
    UserRepository.add_user(User(name=name))
    result = UserRepository.get_user_by_name(name)
    assert result[0].name == "nick"


def test_delete_all_users(init):
    UserRepository.delete_all_users()
    result = UserRepository.get_all_users()
    assert result.count() == 0

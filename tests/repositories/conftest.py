import pytest
from api.Repositories.user_repository import UserRepository


@pytest.fixture
def init():
    UserRepository().delete_all_users()
    return 0

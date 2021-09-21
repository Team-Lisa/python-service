from api.models.user import User


def test_version():
    name = "mockname"
    user = User(name)
    assert user.json() == {
        "name": name
    }

from api.models.user import User


def test_model_to_json():
    name = "mockname"
    user = User(name = name)
    assert user.to_json() == {
        "name": name
    }

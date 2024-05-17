from .user_model import User
from .users_service import UsersService


def test_returns_user_list(create_mock_session):
    mock_users = [
        User(id="uid1", email="email1"),
        User(id="uid2", email="email2"),
    ]
    db = create_mock_session(mock_users)
    users_service = UsersService(db)
    users = users_service.get_users()
    assert users == mock_users


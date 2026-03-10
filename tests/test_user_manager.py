from app.user_manager import get_user

def test_get_user():
    assert get_user() == "admin"
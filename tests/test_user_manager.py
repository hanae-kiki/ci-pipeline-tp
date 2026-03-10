import pytest
from app.user_manager import UserManager


def test_add_user():
    manager = UserManager()
    manager.add_user("hanae-kiki")

    assert manager.count_users() == 1


def test_add_existing_user():
    manager = UserManager()
    manager.add_user("hanae-kiki")

    with pytest.raises(ValueError):
        manager.add_user("hanae-kiki")


def test_remove_user():
    manager = UserManager()
    manager.add_user("oumaima")
    manager.remove_user("oumaima")

    assert manager.count_users() == 0


def test_remove_unknown_user():
    manager = UserManager()

    with pytest.raises(ValueError):
        manager.remove_user("saad")
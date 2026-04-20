import os, pytest
os.environ.setdefault("FLASK_SECRET_KEY", "test-secret")

from auth import MOCK_USERS, check_credentials, get_user

def test_check_credentials_valid():
    assert check_credentials("support", "support123") is True

def test_check_credentials_invalid():
    assert check_credentials("support", "verkeerd") is False

def test_check_credentials_unknown_user():
    assert check_credentials("onbekend", "wachtwoord") is False

def test_get_user_returns_user_info():
    user = get_user("developer")
    assert user is not None
    assert user["role"] == "developer"

def test_get_user_unknown_returns_none():
    assert get_user("onbekend") is None

def test_mock_users_has_three_users():
    assert len(MOCK_USERS) == 3

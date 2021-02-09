import pytest
from app.usecases import CreateUser
from app.entities import InvalidEmail, User, UserAlreadyExists


def test_invalid_email(mocker):
    # Given
    db = mocker.MagicMock()
    cat = mocker.MagicMock()

    # When
    with pytest.raises(InvalidEmail):
        CreateUser(db, cat).execute("not-an-email")

    # Then
    cat.get.assert_not_called()
    db.add.assert_not_called()


def test_create_user(mocker):
    # Given
    db = mocker.MagicMock()
    cat = mocker.MagicMock()
    user = User(email="email@domain.url", cat="http://my-uri.url")
    db.get.return_value = None
    cat.get.return_value = user.cat

    # When
    out = CreateUser(db, cat).execute(user.email)

    # Then
    assert out == user
    db.get.assert_called_once_with(user.email)
    db.add.assert_called_once_with(user)


def test_existing_user(mocker):
    # Given
    db = mocker.MagicMock()
    cat = mocker.MagicMock()
    existing_user = User(email="email@domain.url", cat="http://my-uri.url")
    db.get.return_value = existing_user

    # When
    with pytest.raises(UserAlreadyExists):
        CreateUser(db, cat).execute(existing_user.email)

    # Then
    cat.get.assert_not_called()
    db.add.assert_not_called()

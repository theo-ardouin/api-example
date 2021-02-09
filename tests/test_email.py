from pytest import mark, raises
from app.usecases.email import convert
from app.entities import InvalidEmail


@mark.parametrize("email", ["my@email.url", "a@b.e", "AN@EMAIL.COM"])
def test_valid(email):
    assert convert(email) == email.lower()


@mark.parametrize("email", ["1@email.url", "a@b", "not-an-email", ""])
def test_not_valid(email):
    with raises(InvalidEmail):
        convert(email)

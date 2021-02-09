import re
from app.entities import Email, InvalidEmail


def convert(email: str) -> Email:
    email = email.lower()
    if not re.match("[a-z]+@[a-z]+\.[a-z]+", email):
        raise InvalidEmail()

    return Email(email)

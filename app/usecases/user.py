from typing import Sequence
from app.interfaces import IUser, ICatApi
from app.entities import User, InvalidEmail, UserNotFound, UserAlreadyExists, Email

from .email import convert


class CreateUser:
    def __init__(self, user: IUser, cat: ICatApi) -> None:
        self.user = user
        self.cat = cat

    def execute(self, email: str) -> User:
        email = convert(email)

        if self.user.get(email):
            raise UserAlreadyExists()

        user = User(email=email, cat=self.cat.get())
        self.user.add(user)
        return user


class GetUser:
    def __init__(self, user: IUser) -> None:
        self.user = user

    def execute(self, email: str) -> User:
        email = convert(email)

        user = self.user.get(email)
        if not user:
            raise UserNotFound()

        return user


class GetEmails:
    def __init__(self, user: IUser) -> None:
        self.user = user

    def execute(self) -> Sequence[Email]:
        # Bad design here. Should use cursor rather than dumping all
        return list(self.user.get_emails())

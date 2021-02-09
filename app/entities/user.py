from dataclasses import dataclass
from typing import NewType
from .email import Email

Uri = NewType("Uri", str)


class UserNotFound(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


@dataclass(frozen=True)
class User:
    email: Email
    cat: Uri

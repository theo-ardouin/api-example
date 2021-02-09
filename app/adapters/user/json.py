from json import dump, load
from dataclasses import asdict
from typing import Dict, Iterable, Optional, IO
from app.entities import User, Email, Uri
from app.interfaces import IUserDatabase


class JsonUser(IUserDatabase):
    def __init__(self, handler: IO) -> None:
        self.handler = handler
        self.users = {
            Email(item["email"]): User(email=Email(item["email"]), cat=Uri(item["cat"]))
            for item in load(self.handler)
        }

    def add(self, user: User) -> None:
        self.users[user.email] = user

    def get(self, email: Email) -> Optional[User]:
        return self.users.get(email)

    def get_emails(self) -> Iterable[Email]:
        return self.users.keys()

    def commit(self) -> None:
        self.handler.seek(0)
        dump([asdict(user) for user in self.users.values()], self.handler)
        self.handler.truncate()

    def close(self) -> None:
        self.handler.close()

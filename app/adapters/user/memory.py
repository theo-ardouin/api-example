from typing import Dict, Iterable, Optional
from app.entities import User, Email
from app.interfaces import IUserDatabase


class MemoryUser(IUserDatabase):
    users: Dict[Email, User] = {}

    def add(self, user: User) -> None:
        self.users[user.email] = user

    def get(self, email: Email) -> Optional[User]:
        return self.users.get(email)

    def get_emails(self) -> Iterable[Email]:
        return self.users.keys()

    def commit(self) -> None:
        pass

    def close(self) -> None:
        pass

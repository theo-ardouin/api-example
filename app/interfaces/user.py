from abc import ABC, abstractmethod
from typing import Iterable, Optional
from app.entities import User, Email


class IDatabase(ABC):
    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class IUser(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get(self, email: Email) -> Optional[User]:
        pass

    @abstractmethod
    def get_emails(self) -> Iterable[Email]:
        pass


class IUserDatabase(IDatabase, IUser):
    pass

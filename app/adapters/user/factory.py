from typing import Iterator, Any, Type
from contextlib import contextmanager
from app.interfaces import IUserDatabase, IUser


@contextmanager
def create(cls: Type[IUserDatabase], *args: Any) -> Iterator[IUser]:
    db = cls(*args)
    yield db
    try:
        db.commit()
    finally:
        db.close()

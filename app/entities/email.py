from typing import NewType

Email = NewType("Email", str)


class InvalidEmail(Exception):
    pass

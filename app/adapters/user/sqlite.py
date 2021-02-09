from sqlite3 import Connection
from typing import Iterable, Optional
from app.entities import User, Email, Uri
from app.interfaces import IUserDatabase


class SqlUser(IUserDatabase):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.create_tables()

    def add(self, user: User) -> None:
        self.connection.execute(
            "INSERT INTO users (email, cat) VALUES (?, ?)",
            (user.email, user.cat),
        )

    def get(self, email: Email) -> Optional[User]:
        row = (
            self.connection.cursor()
            .execute("SELECT * FROM users WHERE email = ?", (email,))
            .fetchone()
        )
        return User(email=Email(row[0]), cat=Uri(row[1])) if row else None

    def get_emails(self) -> Iterable[Email]:
        return [
            Email(row[0])
            for row in self.connection.cursor().execute("SELECT email FROM users")
        ]

    def commit(self) -> None:
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def create_tables(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
	            email TEXT PRIMARY KEY NOT NULL UNIQUE,
	            cat TEXT NOT NULL
            );
            """
        )

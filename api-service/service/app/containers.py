"""Module with common containers (dataclasses)."""

from dataclasses import dataclass

__all__ = ['PostgresConnectionParams']


@dataclass
class PostgresConnectionParams:
    """Container with connection parameters for Postgres access.

    Args:
        host: host address
        port: port number
        user: username in Postgres
        password: user password
        dbname: Postgres database name

    """

    host: str
    port: int
    user: str
    password: str
    dbname: str

    @property
    def connection_string(self) -> str:
        """Return line with database connection for sqlalchemy via asyncpg.

        Returns: str

        """
        return (
            f'postgresql+asyncpg://{self.user}:{self.password}@'
            f'{self.host}:{self.port}/{self.dbname}'
        )

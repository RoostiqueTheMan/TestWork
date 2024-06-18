"""Module with async session creator."""
import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from service.app.containers import PostgresConnectionParams

load_dotenv()
__all__ = ['Connection', 'get_session']


class Connection:
    """Class for creating async session."""

    def __init__(self) -> None:
        """Initialize class method.

        Returns: None
        """
        self.__parameters = PostgresConnectionParams(
            host=os.getenv('POSTGRES_HOST'),
            port=int(os.getenv('POSTGRES_PORT')),
            dbname=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )
        self.__engine = create_async_engine(
            self.__parameters.connection_string,
            echo=False
        )
        self.__async_session = sessionmaker(
            bind=self.__engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    @property
    def async_session(self) -> AsyncSession:
        """Return async session.

        Returns: AsyncSession

        """
        return self.__async_session()


async def get_session() -> AsyncSession:
    """Return async session context.

    Returns: AsyncSession

    """
    conn = Connection()
    async with conn.async_session as session:
        yield session

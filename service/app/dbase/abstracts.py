"""Module with abstract base class for DAL."""

from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession


class TableDAL(ABC):
    """Base class for dbase tables."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize class instance.

        Args:
            session: AsyncSession

        Returns: None
        """
        self.__session = session

    @property
    def session(self) -> AsyncSession:
        """Return AsyncSession object.

        Returns: AsyncSession object
        """
        return self.__session

    async def is_query_success(self) -> bool:
        """Check that changing query is success.

        Returns: True if query success, otherwise - False
        """
        try:
            await self.session.commit()
            return True

        except DBAPIError:
            await self.session.rollback()
            return False

    @abstractmethod
    async def get_all(self) -> List[object]:
        """Get all records from table.

        Returns: list with ORM models
        """
        pass

"""Module with abstract base class for DAL."""

from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

__all__ = ['TableDAL']


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

    @abstractmethod
    async def get_all(self) -> List[object]:
        """Get all records from table.

        Returns: list with ORM models
        """
        pass

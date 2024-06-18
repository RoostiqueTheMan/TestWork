"""Module with Data table DAL class."""

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.abstracts import TableDAL
from app.dbase.orm import Client, Customer, User
from app.decorators import check_timeout
from app.models import IdNameInfo

__all__ = ['UserDAL', 'ClientDAL', 'CustomerDAL']


class CommonTableDAL:
    """Common class for dbase tables."""

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

class UserDAL(TableDAL):
    """User table DAL class."""

    @check_timeout
    async def get_all(self) -> List[Optional[IdNameInfo]]:
        """Get all records from users table.

        Returns: list with Pydantic models
        """
        try:
            records = (
                await self.session.execute(select(User))
            ).scalars().all()

        except SQLAlchemyError:
            records = []

        return [
            IdNameInfo(id_=record.id_, name=record.name) for record in records
        ]


class ClientDAL(TableDAL):
    """Client table DAL class."""

    @check_timeout
    async def get_all(self) -> List[Optional[IdNameInfo]]:
        """Get all records from clients table.

        Returns: list with Pydantic models
        """
        try:
            records = (
                await self.session.execute(select(Client))
            ).scalars().all()

        except SQLAlchemyError:
            records = []

        return [
            IdNameInfo(id_=record.id_, name=record.name) for record in records
        ]


class CustomerDAL(TableDAL):
    """Customer table DAL class."""

    @check_timeout
    async def get_all(self) -> List[Optional[IdNameInfo]]:
        """Get all records from customers table.

        Returns: list with Pydantic models
        """
        try:
            records = (
                await self.session.execute(select(Customer))
            ).scalars().all()

        except SQLAlchemyError:
            records = []

        return [
            IdNameInfo(id_=record.id_, name=record.name) for record in records
        ]

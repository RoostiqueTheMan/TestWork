"""Module with Data table DAL class."""

from typing import List, Optional

from sqlalchemy import select

from service.app.dbase.abstracts import TableDAL
from service.app.dbase.orm import Client, Customer, User
from service.app.decorators import check_timeout
from service.app.models import IdNameInfo
from sqlalchemy.exc import SQLAlchemyError

__all__ = ['UserDAL', 'ClientDAL', 'CustomerDAL']


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

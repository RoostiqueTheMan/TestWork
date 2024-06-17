"""Module with Data table DAL class."""

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.abstracts import TableDAL
from app.dbase.orm import Client, Customer, User
from app.models import CommonData


class UserDAL(TableDAL):
    """User table DAL class."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize method.

        Args:
            session: sqlalchemy AsyncSession

        Returns: None
        """
        super().__init__(session=session)

    async def get_all(self) -> List[Optional[CommonData]]:
        """Get all records from users table.

        Returns: list with Pydantic models
        """
        records = (await self.session.execute(select(User))).scalars().all()

        return [
            CommonData(id_=record.id_, name=record.name) for record in records
        ]


class ClientDAL(TableDAL):
    """Client table DAL class."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize method.

        Args:
            session: sqlalchemy AsyncSession

        Returns: None
        """
        super().__init__(session=session)

    async def get_all(self) -> List[Optional[CommonData]]:
        """Get all records from clients table.

        Returns: list with Pydantic models
        """
        records = (await self.session.execute(select(Client))).scalars().all()

        return [
            CommonData(id_=record.id_, name=record.name) for record in records
        ]


class CustomerDAL(TableDAL):
    """Customer table DAL class."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize method.

        Args:
            session: sqlalchemy AsyncSession

        Returns: None
        """
        super().__init__(session=session)

    async def get_all(self) -> List[Optional[CommonData]]:
        """Get all records from customers table.

        Returns: list with Pydantic models
        """
        records = (
            await self.session.execute(select(Customer))
        ).scalars().all()

        return [
            CommonData(id_=record.id_, name=record.name) for record in records
        ]

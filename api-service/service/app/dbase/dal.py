"""Module with Data table DAL class."""

from typing import List, Optional, Union

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.orm import Client, Customer, User
from app.decorators import check_timeout
from app.models import IdNameInfo

__all__ = ['CommonDAL']


class CommonDAL:
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

    @check_timeout
    async def get_all(
            self,
            table: Union[Client, Customer, User]
    ) -> List[Optional[IdNameInfo]]:
        """Get all records from users table.

        Args:
            table: orm model name

        Returns: list with Pydantic models
        """
        try:
            records = (
                await self.session.execute(select(table))
            ).scalars().all()

        except SQLAlchemyError:
            records = []

        return [
            IdNameInfo(id_=record.id_, name=record.name) for record in records
        ]

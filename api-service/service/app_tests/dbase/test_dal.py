"""Module with DAL classes tests."""
from typing import Union
from unittest.mock import Mock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.dal import CommonDAL
from app.dbase.orm import Client, Customer, User
from app.models import IdNameInfo


class TestCommonDAL:
    """Class with CommonDAL tests."""

    def test_session(self):
        """Test session property."""
        session = AsyncSession()

        assert CommonDAL(session=session).session == session

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'table', [Client, Customer, User]
    )
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(
            self,
            mock_execute: Mock,
            table: Union[Client, Customer, User]
    ):
        """Test get_all method.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        expected_value = [IdNameInfo(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records

        actual_value = await CommonDAL(session=session).get_all(table=table)

        assert actual_value == expected_value

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'table', [Client, Customer, User]
    )
    @patch.object(AsyncSession, 'execute')
    async def test_get_all_with_exception(
            self,
            mock_execute: Mock,
            table: Union[Client, Customer, User]
    ):
        """Test get_all method with exception.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        mock_execute.side_effect = SQLAlchemyError
        actual_value = await CommonDAL(session=session).get_all(table=table)

        assert actual_value == []

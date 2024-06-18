"""Module with DAL classes tests."""
from unittest.mock import Mock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from service.app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from service.app.models import IdNameInfo
from sqlalchemy.exc import SQLAlchemyError


class TestUserDAL:
    """Class with UserDAL tests."""

    def test_session(self):
        """Test session property."""
        session = AsyncSession()

        assert UserDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        """Test get_all method.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        expected_value = [IdNameInfo(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records

        actual_value = await UserDAL(session=session).get_all()

        assert actual_value == expected_value

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all_with_exception(self, mock_execute: Mock):
        """Test get_all method with exception.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        mock_execute.side_effect = SQLAlchemyError
        actual_value = await UserDAL(session=session).get_all()

        assert actual_value == []


class TestClientDAL:
    """Class with ClientDAL tests."""

    def test_session(self):
        """Test session property."""
        session = AsyncSession()

        assert ClientDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        """Test get_all method.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        expected_value = [IdNameInfo(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records

        actual_value = await ClientDAL(session=session).get_all()

        assert actual_value == expected_value

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all_with_exception(self, mock_execute: Mock):
        """Test get_all method with exception.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        mock_execute.side_effect = SQLAlchemyError
        actual_value = await ClientDAL(session=session).get_all()

        assert actual_value == []


class TestCustomerDAL:
    """Class with CustomerDAL tests."""

    def test_session(self):
        """Test session property."""
        session = AsyncSession()

        assert ClientDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        """Test get_all method.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        expected_value = [IdNameInfo(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records

        actual_value = await CustomerDAL(session=session).get_all()

        assert actual_value == expected_value

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all_with_exception(self, mock_execute: Mock):
        """Test get_all method with exception.

        Args:
            mock_execute: mocking sqlalchemy execute method
        """
        session = AsyncSession()
        mock_execute.side_effect = SQLAlchemyError
        actual_value = await CustomerDAL(session=session).get_all()

        assert actual_value == []

from unittest.mock import Mock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from app.models import CommonData


class TestUserDAL:

    def test_session(self):
        session = AsyncSession()

        assert UserDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records
        user_dal = UserDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value


class TestClientDAL:

    def test_session(self):
        session = AsyncSession()

        assert ClientDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records
        user_dal = ClientDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value


class TestCustomerDAL:

    def test_session(self):
        session = AsyncSession()

        assert UserDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=i, name=f'test{i}') for i in range(5)]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records
        user_dal = CustomerDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value

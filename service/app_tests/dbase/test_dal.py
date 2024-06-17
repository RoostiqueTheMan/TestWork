from unittest.mock import MagicMock, Mock, patch

import pytest
from app.dbase.dal import UserDAL
from app.models import CommonData
from sqlalchemy.ext.asyncio import AsyncSession


class TestUserDAL:

    def test_session(self):
        session = Mock()

        assert UserDAL(session=session).session == session

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=1, name='test')]
        mock_scalars = MagicMock()
        mock_scalars.return_value.scalars_return_value = expected_value
        mock_execute.return_value = mock_scalars
        user_dal = UserDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all2(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=1, name='test')]

        records = Mock()
        records.scalars.return_value = expected_value
        mock_execute.return_value = records
        user_dal = UserDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value

    @pytest.mark.asyncio
    @patch.object(AsyncSession, 'execute')
    async def test_get_all3(self, mock_execute: Mock):
        session = AsyncSession()
        expected_value = [CommonData(id_=1, name='test')]

        records = Mock()
        records.scalars.return_value.all.return_value = expected_value
        mock_execute.return_value = records
        user_dal = UserDAL(session=session)

        result = await user_dal.get_all()

        assert result == expected_value

"""Module with tests for routers."""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from app.dbase.dal import CommonDAL
from app.models import IdNameInfo, Response
from app.routers.records import get_all_records


class TestRecords:
    """Test records routers class."""

    @pytest.mark.asyncio
    @patch.object(CommonDAL, 'get_all')
    async def test_get_all_records(
            self,
            mock_get_all: Mock
    ):
        """Test get_all_records route, check correct response structure...

        (records ids increasing)

        Args:
            mock_get_all: mock get_all method
        """
        users = [
            IdNameInfo(id_=i, name=f'test-{i}') for i in range(3)
        ]
        clients = [
            IdNameInfo(id_=i, name=f'test-{i}') for i in range(9, 3, -1)
        ]
        customers = [
            IdNameInfo(id_=i, name=f'test-{i}') for i in range(20, 9, -1)
        ]
        expected_value = []
        expected_value.extend(users)
        expected_value.extend(clients)
        expected_value.extend(customers)
        expected_value.sort(key=lambda data: data.id_)
        mock_get_all.side_effect = [users, clients, customers]

        response = await get_all_records(session=AsyncMock())

        assert response == Response(data=expected_value)

        for i in range(len(response.data)):
            assert response.data[i] == expected_value[i]

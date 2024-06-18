"""Module with tests for routers."""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from service.app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from service.app.models import IdNameInfo, Response
from service.app.routers.records import get_all_records


class TestRecords:
    """Test records routers class."""

    @pytest.mark.asyncio
    @patch.object(UserDAL, 'get_all')
    @patch.object(ClientDAL, 'get_all')
    @patch.object(CustomerDAL, 'get_all')
    async def test_get_all_records(
            self,
            get_all_customers: Mock,
            get_all_clients: Mock,
            get_all_users: Mock
    ):
        """Test get_all_records route, check correct response structure...

        (records ids increasing)

        Args:
            get_all_customers: mock get_all method
            get_all_users: mock get_all method
            get_all_clients: mock get_all method
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

        get_all_users.return_value = users
        get_all_clients.return_value = clients
        get_all_customers.return_value = customers

        response = await get_all_records(session=AsyncMock())

        assert response == Response(data=expected_value)

        for i in range(len(response.data)):
            assert response.data[i] == expected_value[i]

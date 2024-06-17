from unittest.mock import Mock, patch, AsyncMock

import pytest

from app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from app.models import CommonData

from app.routers.records import get_all_records
from app.models import Response


class TestRecords:
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
        users = [
            CommonData(id_=i, name=f'test-{i}') for i in range(3)
        ]
        clients = [
            CommonData(id_=i, name=f'test-{i}') for i in range(3, 6)
        ]
        customers = [
            CommonData(id_=i, name=f'test-{i}') for i in range(6, 9)
        ]
        expected_value = []
        expected_value.extend(users)
        expected_value.extend(clients)
        expected_value.extend(customers)

        get_all_users.return_value = users
        get_all_clients.return_value = clients
        get_all_customers.return_value = customers

        response = await get_all_records(session=AsyncMock())

        assert response == Response(data=expected_value)

        for i in range(len(response.data)):
            assert response.data[i] == expected_value[i]

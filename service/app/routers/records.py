"""Module with FastAPI routers."""

from asyncio import TimeoutError, wait_for

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from app.dbase.session import get_session
from app.models import Response

router = APIRouter()
TIMEOUT = 2


@router.get('/get-all')
async def get_all_records(
        session: AsyncSession = Depends(get_session)
) -> Response:
    """Get all records from dbase.

    Args:
        session: sqlalchemy AsyncSession

    Returns: list with data records
    """
    try:
        users = await wait_for(UserDAL(session=session).get_all(), TIMEOUT)
    except TimeoutError:
        users = []

    try:
        clients = await wait_for(ClientDAL(session=session).get_all(), TIMEOUT)
    except TimeoutError:
        clients = []

    try:
        customers = await wait_for(
            CustomerDAL(session=session).get_all(),
            TIMEOUT
        )
    except TimeoutError:
        customers = []

    users.extend(clients)
    users.extend(customers)
    users.sort(key=lambda data: data.id_)

    return Response(data=users)

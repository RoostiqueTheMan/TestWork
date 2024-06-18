"""Module with FastAPI routers."""

from fastapi import APIRouter, Depends
from service.app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from service.app.dbase.session import get_session
from service.app.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

__all__ = ['router']

router = APIRouter()
TIMEOUT = 2


@router.get('/get-all')
async def get_all_records(
        session: AsyncSession = Depends(get_session)
) -> Response:
    """Get all records from dbase by index increasing.

    Args:
        session: sqlalchemy AsyncSession

    Returns: list with data records
    """
    users = await UserDAL(session=session).get_all()
    clients = await ClientDAL(session=session).get_all()
    customers = await CustomerDAL(session=session).get_all()

    users.extend(clients)
    users.extend(customers)
    users.sort(key=lambda data: data.id_)

    return Response(data=users)
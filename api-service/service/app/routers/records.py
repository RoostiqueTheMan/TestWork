"""Module with FastAPI routers."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.dal import CommonDAL
from app.dbase.orm import Client, Customer, User
from app.dbase.session import get_session
from app.models import Response

__all__ = ['router']

router = APIRouter()


@router.get('/get-all')
async def get_all_records(
        session: AsyncSession = Depends(get_session)
) -> Response:
    """Get all records from dbase by index increasing.

    Args:
        session: sqlalchemy AsyncSession

    Returns: list with data records
    """
    dal = CommonDAL(session=session)
    users = await dal.get_all(table=User)
    clients = await dal.get_all(table=Client)
    customers = await dal.get_all(table=Customer)

    users.extend(clients)
    users.extend(customers)
    users.sort(key=lambda data: data.id_)

    return Response(data=users)

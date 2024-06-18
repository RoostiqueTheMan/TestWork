"""Module with decorators."""

from typing import Callable, List, Optional
from app.models import IdNameInfo
from asyncio import wait_for, TimeoutError

__all__ = ['check_timeout']
TIMEOUT = 2


def check_timeout(func: Callable) -> Callable:
    """Decorator function."""

    async def wrapper(*args) -> List[Optional[IdNameInfo]]:
        """Check query executing time.

        Returns: list with pydantic models
        """
        try:
            records = await wait_for(func(*args), TIMEOUT)

        except TimeoutError:
            records = []

        return records

    return wrapper

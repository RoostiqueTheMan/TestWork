"""Module with decorators."""

from asyncio import TimeoutError, wait_for
from typing import Callable, List, Optional

from service.app.models import IdNameInfo

__all__ = ['check_timeout']

TIMEOUT = 2


def check_timeout(func: Callable) -> Callable:
    """Decorate function."""

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

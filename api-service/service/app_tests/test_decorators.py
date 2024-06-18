"""Module with decorators tests."""
import asyncio
from typing import List, Optional

import pytest

from app.decorators import TIMEOUT, check_timeout


class TestDecorator:
    """Decorator test class."""

    @staticmethod
    async def mock_function(timeout: float) -> List[str]:
        """Mock function with timeout.

        Args:
            timeout: timeout in seconds

        Returns: None
        """
        await asyncio.sleep(timeout)

        return ['test']

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ['timeout', 'expected_value'],
        [
            (TIMEOUT - 1, ['test']),
            (TIMEOUT - 0.1, ['test']),
            (TIMEOUT + 0.1, [])
        ]
    )
    async def test_check_timeout(
            self,
            timeout: float,
            expected_value: List[Optional[str]]
    ):
        """Test check_timeout.

        Args:
            timeout: timeout in seconds
            expected_value: expected value

        Returns: None
        """
        decorated_func = check_timeout(func=self.mock_function)
        actual_value = await decorated_func(timeout)

        assert actual_value == expected_value

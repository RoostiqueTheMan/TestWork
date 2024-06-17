from unittest.mock import Mock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.dbase.dal import ClientDAL, CustomerDAL, UserDAL
from app.models import CommonData

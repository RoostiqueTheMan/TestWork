"""Module with Pydantic models."""

from typing import List

from pydantic import BaseModel, Field

__all__ = ['IdNameInfo', 'Response']


class CustomBaseModel(BaseModel):
    """Pydantic custom base model."""

    class Config:
        """Model configuration."""

        populate_by_name = True


class IdNameInfo(CustomBaseModel):
    """Class with common tables data.

    Args:
        id_: id
        name: name

    """

    id_: int = Field(alias='ID')
    name: str = Field(alias='Name', min_length=1, max_length=30)


class Response(CustomBaseModel):
    """Class with response model.

    Args:
        status: request status
        data: list with Pydantic models
    """

    status: bool = Field(alias='Status', default=True)
    data: List[IdNameInfo] = Field(alias='Data')

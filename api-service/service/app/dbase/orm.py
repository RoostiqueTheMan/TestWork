"""Module with SQLAlchemy ORM models for database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

__all__ = ['User', 'Client', 'Customer']


class Base(DeclarativeBase):
    """Base ORM class."""

    id_ = Column(
        name='id',
        type_=Integer,
        primary_key=True,
        index=True
    )
    name = Column(
        name='name',
        type_=String(length=30),
        nullable=False,
        unique=True
    )


class User(Base):
    """User table ORM model."""

    __tablename__ = 'users'


class Client(Base):
    """Client table ORM model."""

    __tablename__ = 'clients'


class Customer(Base):
    """Customer table ORM model."""

    __tablename__ = 'customers'

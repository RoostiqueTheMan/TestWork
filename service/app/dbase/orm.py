"""Module with SQLAlchemy ORM models for database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base ORM class."""

    id_ = Column(
        name='id',
        type_=Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    name = Column(
        name='name',
        type_=String(length=30),
        nullable=False,
        unique=True
    )


class User(Base):
    """User table model."""

    __tablename__ = 'users'


class Client(Base):
    """Client table model."""

    __tablename__ = 'clients'


class Customer(Base):
    """Customer table model."""

    __tablename__ = 'customers'

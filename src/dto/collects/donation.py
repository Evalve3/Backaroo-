from _decimal import Decimal
from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.collects.collect import Collect
from src.dto.user.user import User


class Gift(BaseModel, BaseEntity):
    name: str
    description: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class Donation(BaseModel, BaseEntity):
    collect: Collect
    author: User
    amount: Decimal
    create_date: datetime
    status: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class DonationStatus(Enum):
    OK = "OK"
    CANCELED = "CANCELED"
    PENDING = "PENDING"

    @classmethod
    def from_string(cls, value: str):
        return cls(value)

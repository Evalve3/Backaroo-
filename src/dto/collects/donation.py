from datetime import datetime

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
    amount: float
    create_date: datetime.date
    status: bool
    gift: Gift

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

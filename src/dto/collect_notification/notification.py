import datetime

from pydantic import BaseModel, Field

from src.dto.base_dto import BaseEntity
from src.dto.collects.collect import Collect
from src.dto.user.user import User


class SubscribeNotification(BaseModel, BaseEntity):
    collect: Collect
    user: User
    create_date: datetime.datetime

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class Notification(BaseModel, BaseEntity):
    subscribe: SubscribeNotification
    text: str
    create_date: datetime.datetime
    status: bool

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)



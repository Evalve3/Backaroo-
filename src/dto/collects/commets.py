import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.collects.collect import Collect
from src.dto.user.user import User


class Comment(BaseModel, BaseEntity):
    author: User
    text: str
    create_date: datetime.datetime
    collect: Collect

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

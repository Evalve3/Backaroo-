import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.category.category import SupportCategory
from src.dto.collects.collect import Collect
from src.dto.user.user import User


class SupportQuestion(BaseModel, BaseEntity):
    author: User
    create_date: datetime.datetime
    status: bool
    category: SupportCategory
    collect: Collect
    text: str
    need_answer: bool

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

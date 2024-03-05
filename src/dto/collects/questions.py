import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.collects.collect import Collect
from src.dto.user.user import User


class Question(BaseModel, BaseEntity):
    author: User
    text: str
    create_date: datetime.datetime
    collect: Collect

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class QuestionAnswer(BaseModel, BaseEntity):
    question: Question
    author: User
    text: str
    create_date: datetime.datetime

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

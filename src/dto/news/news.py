import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.collects.collect import Collect


class News(BaseModel, BaseEntity):
    name: str
    text: str
    create_date: datetime.datetime
    collect: Collect

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

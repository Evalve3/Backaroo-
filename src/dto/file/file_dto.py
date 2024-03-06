from datetime import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.category.category import CollectCategory, Country


class File(BaseModel, BaseEntity):
    name: str
    data: bytes

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

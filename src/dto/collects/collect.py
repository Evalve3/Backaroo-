import uuid
from _decimal import Decimal
from datetime import datetime
from enum import Enum
from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.category.category import CollectCategory, Country
from src.dto.user.user import User


class Collect(BaseModel, BaseEntity):
    name: str
    description: str
    target_amount: Decimal
    current_amount: Decimal
    category: CollectCategory
    create_date: datetime
    status: bool
    country: Country
    image_uid: uuid.UUID
    author: User

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)



class CollectSortParameter(Enum):
    NAME = "name"
    TARGET_AMOUNT = "target_amount"
    CURRENT_AMOUNT = "current_amount"
    CREATE_DATE = "create_date"
    STATUS = "status"
    COUNTRY = "country"
    CATEGORY = "category"
    AUTHOR = "author"

    @classmethod
    def from_string(cls, value: str):
        return cls(value)


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

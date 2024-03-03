from datetime import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity
from src.dto.category.category import CollectCategory, Country


class Collect(BaseModel, BaseEntity):
    name: str
    description: str
    target_amount: float
    current_amount: float
    category: CollectCategory
    create_date: datetime.date
    status: bool
    country: Country

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

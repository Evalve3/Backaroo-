import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, Field

from src.dto.base_dto import BaseEntity
from src.dto.category.category import Country


class User(BaseModel, BaseEntity):
    username: str
    first_name: str
    last_name: str
    date_birth: datetime.date
    email: str

    avatar: Optional[uuid.UUID] = Field(default=None)
    profile_status: Optional[str] = Field(default=None)
    additional_info: Optional[str] = Field(default=None)
    sex: Optional[bool] = Field(default=None)
    adult_content: Optional[bool] = Field(default=None)
    registration_date: Optional[datetime.datetime] = Field(default_factory=datetime.datetime.now)
    country: Optional[Country] = Field(default=None)

    # After creation
    is_active: bool = Field(default=True)
    hashed_password: Optional[str] = Field(default=None)

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

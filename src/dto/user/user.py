import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, Field

from src.dto.base_dto import BaseEntity


class User(BaseModel, BaseEntity):
    username: str
    first_name: str
    last_name: str
    date_birth: datetime.date
    email: str

    avatar: Optional[str] = Field(default=None)

    # After creation
    is_active: bool = Field(default=True)
    uid: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4)
    hashed_password: Optional[str] = Field(default=None)

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

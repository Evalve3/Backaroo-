from datetime import datetime

from pydantic import BaseModel

from src.dto.base_dto import BaseEntity


class User(BaseModel, BaseEntity):
    username: str
    first_name: str
    last_name: str
    date_birth: datetime
    email: str

    avatar: str = None

    # After creation
    is_active: bool = None
    uid: str = None
    hashed_password: str = None

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

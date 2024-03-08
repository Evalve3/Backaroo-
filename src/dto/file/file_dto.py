from pydantic import BaseModel

from src.dto.base_dto import BaseEntity


class File(BaseModel, BaseEntity):
    name: str
    data: bytes

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

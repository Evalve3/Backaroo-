from pydantic import BaseModel, Field

from src.dto.base_dto import BaseEntity


class Country(BaseModel, BaseEntity):
    name: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class CollectCategory(BaseModel, BaseEntity):
    name: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)


class SupportCategory(BaseModel, BaseEntity):
    name: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(**other)

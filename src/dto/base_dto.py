import uuid
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional

from pydantic import Field


@dataclass
class BaseEntity(metaclass=ABCMeta):
    uid: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4)

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        pass

    @abstractmethod
    def dict(self):
        pass

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseEntity(metaclass=ABCMeta):
    uid: Optional[str]

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        pass

    @abstractmethod
    def dict(self):
        pass

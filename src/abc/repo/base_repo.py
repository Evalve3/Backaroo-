from abc import ABC, abstractmethod
from typing import Optional, Iterable

from src.dto.user.user import BaseEntity


class BaseAsyncReadOnlyRepository(ABC):
    @abstractmethod
    async def get(self, uid: str) -> Optional[BaseEntity]:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> Iterable[BaseEntity]:
        pass


class BaseAsyncWriteOnlyRepository(ABC):
    @abstractmethod
    async def create(self, other: BaseEntity) -> BaseEntity:
        pass

    @abstractmethod
    async def delete(self, uid: str) -> bool:
        pass

    @abstractmethod
    async def update(self, uid: str, other: BaseEntity) -> BaseEntity:
        pass


class BaseAsyncRepository(BaseAsyncReadOnlyRepository, BaseAsyncWriteOnlyRepository, ABC):
    pass

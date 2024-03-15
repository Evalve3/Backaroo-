import uuid
from abc import ABC, abstractmethod
from typing import Optional, Iterable

from src.dto.user.user import BaseEntity


class BaseAsyncReadOnlyRepository(ABC):
    @abstractmethod
    async def get(self, uid: uuid.UUID) -> Optional[BaseEntity]:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> Iterable[BaseEntity]:
        #  kwargs can be used for filtering (e.g. name='John')
        pass


class BaseAsyncWriteOnlyRepository(ABC):
    @abstractmethod
    async def create(self, other: BaseEntity) -> BaseEntity:
        pass

    @abstractmethod
    async def delete(self, uid: uuid.UUID) -> bool:
        pass

    @abstractmethod
    async def update(self, uid: uuid.UUID, other: BaseEntity) -> BaseEntity:
        pass


class BaseAsyncRepository(BaseAsyncReadOnlyRepository, BaseAsyncWriteOnlyRepository, ABC):
    pass

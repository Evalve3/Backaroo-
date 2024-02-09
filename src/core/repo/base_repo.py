from abc import ABC, abstractmethod
from typing import Optional, Iterable

from src.dto.user.user import BaseEntity


class AsyncContextManagerRepository(ABC):
    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            print('Rolling back transaction')
            await self.rollback()
        else:
            print('Committing transaction')
            await self.commit()


class BaseAsyncReadOnlyRepository(ABC):
    @abstractmethod
    async def get(self, uid: str) -> Optional[BaseEntity]:
        pass

    @abstractmethod
    async def get_list(self, filter_params: dict) -> Iterable[BaseEntity]:
        pass


class BaseAsyncWriteOnlyRepository(AsyncContextManagerRepository):
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

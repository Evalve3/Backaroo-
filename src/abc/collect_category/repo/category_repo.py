from abc import abstractmethod, ABC
from typing import List
from uuid import UUID

from src.abc.repo.base_repo import BaseAsyncRepository
from src.dto.category.category import CollectCategory


class AsyncCategoryRepository(BaseAsyncRepository, ABC):

    @abstractmethod
    async def get(self, uid: UUID) -> CollectCategory:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> List[CollectCategory]:
        pass

    @abstractmethod
    async def create(self, other: CollectCategory) -> CollectCategory:
        pass

    @abstractmethod
    async def update(self, uid: UUID, category: CollectCategory) -> CollectCategory:
        pass

    @abstractmethod
    async def delete(self, uid: UUID) -> bool:
        pass

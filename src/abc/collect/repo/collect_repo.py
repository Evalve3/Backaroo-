from abc import abstractmethod, ABC
from typing import List
from uuid import UUID

from src.abc.repo.base_repo import BaseAsyncRepository
from src.dto.collects.collect import Collect, CollectSortParameter, SortOrder


class IAsyncCollectRepository(BaseAsyncRepository, ABC):

    @abstractmethod
    async def get(self, uid: UUID) -> Collect:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> List[Collect]:
        pass

    @abstractmethod
    async def get_page(self,
                       sort_by: CollectSortParameter,
                       on_page: int,
                       page: int,
                       sort_order: SortOrder = SortOrder.desc,
                       **kwargs) -> List[Collect]:
        pass

    @abstractmethod
    async def create(self, other: Collect) -> Collect:
        pass

    @abstractmethod
    async def update(self, uid: UUID, collect: Collect) -> Collect:
        pass

    @abstractmethod
    async def delete(self, uid: UUID) -> bool:
        pass

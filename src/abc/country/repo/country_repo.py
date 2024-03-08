from abc import abstractmethod, ABC
from typing import List
from uuid import UUID

from src.abc.repo.base_repo import BaseAsyncRepository
from src.dto.category.category import Country


class AsyncCountryRepository(BaseAsyncRepository, ABC):

    @abstractmethod
    async def get(self, uid: UUID) -> Country:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> List[Country]:
        pass

    @abstractmethod
    async def create(self, other: Country) -> Country:
        pass

    @abstractmethod
    async def update(self, uid: UUID, country: Country) -> Country:
        pass

    @abstractmethod
    async def delete(self, uid: UUID) -> bool:
        pass

from abc import ABC, abstractmethod
from typing import Iterable
from uuid import UUID

from src.abc.repo.base_repo import BaseAsyncRepository
from src.dto.file.file_dto import File


class AsyncFileRepositoryABC(BaseAsyncRepository, ABC):

    @abstractmethod
    async def create(self, file: File) -> File:
        pass

    @abstractmethod
    async def get(self, uid: UUID) -> File:
        pass

    @abstractmethod
    async def delete(self, uid: UUID) -> bool:
        pass

    @abstractmethod
    async def get_list(self, **kwargs) -> Iterable[File]:
        pass

    @abstractmethod
    async def update(self, uid: str, other: File) -> File:
        pass

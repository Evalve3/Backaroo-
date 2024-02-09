from abc import abstractmethod, ABC
from typing import List

from src.core.repo.base_repo import BaseAsyncRepository
from src.dto.user.user import User


class AsyncUserRepository(BaseAsyncRepository, ABC):

    @abstractmethod
    async def get(self, uid: str) -> User:
        pass

    @abstractmethod
    async def get_list(self, filter_params: dict) -> List[User]:
        pass

    @abstractmethod
    async def create(self, other: User) -> User:
        pass

    @abstractmethod
    async def update(self, uid: str, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, uid: str) -> bool:
        pass

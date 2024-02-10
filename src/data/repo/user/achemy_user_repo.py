from typing import List

from src.core.repo.user.user_repo import AsyncUserRepository
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.user.user import User
from src.models.user.user_model import UserModel


class UserRepoAlchemy(BaseSqlAlchemyAsyncRepository, AsyncUserRepository):

    async def get(self, uid: str) -> User:
        user = await self._session.filter(UserModel).where(User.id == uid).first()
        user_dto = User(**user.dict())
        return user_dto

    async def get_list(self, filter_params: dict) -> List[User]:
        pass

    async def create(self, other: User) -> User:
        user = UserModel(**other.dict())
        self._session.add(user)
        user_dto = User(**user.dict())
        return user_dto

    async def update(self, uid: str, user: User) -> User:
        pass

    async def delete(self, uid: str) -> bool:
        pass

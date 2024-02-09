from src.core.repo.user.user_repo import AsyncUserRepository
from src.core.usecase.base_usecase import BaseAsyncUseCase
from src.dto.user.user import User


class CreateUserUC(BaseAsyncUseCase):
    def __init__(self, user_repo: AsyncUserRepository):
        self.user_repo = user_repo

    async def execute(self, user: User) -> User:
        async with self.user_repo as user_repo:
            res = await user_repo.create(user)
            return res

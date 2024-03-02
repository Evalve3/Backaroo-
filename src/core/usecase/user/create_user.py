from src.core.repo.user.user_repo import AsyncUserRepository
from src.core.usecase.base_usecase import BaseAsyncUseCase, Response
from src.dto.user.user import User


class CreateUserUC(BaseAsyncUseCase):
    def __init__(self, user_repo: AsyncUserRepository):
        self.user_repo = user_repo

    async def execute(self, user: User) -> Response:
        created_user = await self.user_repo.create(user)
        return created_user

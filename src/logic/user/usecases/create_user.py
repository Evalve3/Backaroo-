from typing import Union

from src.abc.user.repo.UserRepoExceptions import UniqueViolationException
from src.abc.user.repo.user_repo import AsyncUserRepository
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.dto.user.user import User


class CreateUserUC(BaseAsyncUseCase):
    def __init__(self, user_repo: AsyncUserRepository):
        self.user_repo = user_repo

    async def execute(self, user: User) -> Union[SuccessResponse, ErrorResponse]:
        try:
            created_user = await self.user_repo.create(user)
            return SuccessResponse(data=created_user, code=200)
        except UniqueViolationException as e:
            return ErrorResponse(code=400, error=str(e.ex_data))

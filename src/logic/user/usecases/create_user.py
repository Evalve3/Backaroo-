from dataclasses import dataclass
from typing import Union

from src.abc.repo.base_exceptions import UniqueViolationException
from src.abc.user.repo.user_repo import AsyncUserRepository
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.dto.user.user import User
from src.abc.user.presenters.user.user_presenter import IUserPresenter


@dataclass
class CreateUserDTO:
    user: User


class CreateUserUC(BaseAsyncUseCase):
    def __init__(self,
                 user_repo: AsyncUserRepository,
                 user_presenter: IUserPresenter
                 ):
        self.user_repo = user_repo
        self.user_presenter = user_presenter

    async def execute(self, dto: CreateUserDTO) -> Union[SuccessResponse, ErrorResponse]:
        try:
            created_user = await self.user_repo.create(dto.user)
            presented_user = self.user_presenter.get_user_presentation(created_user)
            return SuccessResponse(data=presented_user, code=200)
        except UniqueViolationException as e:
            return ErrorResponse(code=400, error=str(e.ex_data))

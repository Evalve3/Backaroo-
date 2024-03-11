import datetime
import uuid
from dataclasses import dataclass

from typing import Union

from src.abc.country.repo.country_repo import AsyncCountryRepository
from src.abc.repo.base_exceptions import NotFoundException
from src.abc.repo.base_exceptions import UniqueViolationException
from src.abc.user.repo.user_repo import AsyncUserRepository
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.abc.user.presenters.user_presenter import IUserPresenter
from src.dto.user.user import User


@dataclass
class EditUserDTO:
    user_uid_to_edit: uuid.UUID
    username: str
    first_name: str
    last_name: str
    date_birth: datetime.date
    email: str
    avatar_id: uuid.UUID
    additional_info: str
    sex: bool
    country: str



class EditUserUC(BaseAsyncUseCase):
    def __init__(self,
                 user_repo: AsyncUserRepository,
                 user_presenter: IUserPresenter,
                 country_repo: AsyncCountryRepository
                 ):
        self.user_repo = user_repo
        self.user_presenter = user_presenter
        self.country_repo = country_repo

    async def execute(self, dto: EditUserDTO) -> Union[SuccessResponse, ErrorResponse]:

        if dto.country:
            try:
                country_list = await self.country_repo.get_list(name=dto.country)
            except NotFoundException:
                return ErrorResponse(code=404, error="Country not found")
            if len(country_list) == 0:
                return ErrorResponse(code=404, error="Country not found")
            if len(country_list) > 1:
                return ErrorResponse(code=400, error="Too many countries found")
            country = country_list[0]
        else:
            country = None

        user_for_edit = User(
            uid=dto.user_uid_to_edit,
            username=dto.username,
            first_name=dto.first_name,
            last_name=dto.last_name,
            date_birth=dto.date_birth,
            email=dto.email,
            avatar_id=dto.avatar_id,
            additional_info=dto.additional_info,
            country=country,
            sex=dto.sex,
        )

        try:
            edited_user = await self.user_repo.update(uid=dto.user_uid_to_edit, user=user_for_edit)
        except UniqueViolationException as e:
            return ErrorResponse(code=400, error=str(e.ex_data))
        except NotFoundException:
            return ErrorResponse(code=404, error="User not found")
        presented_user = self.user_presenter.get_user_presentation(edited_user)
        return SuccessResponse(data=presented_user, code=200)

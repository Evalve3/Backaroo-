import datetime
import uuid
from dataclasses import dataclass
from typing import Union

from src.abc.collect.presenters.collect_presenter import ICollectPresenter
from src.abc.collect.repo.collect_repo import IAsyncCollectRepository
from src.abc.collect_category.repo.category_repo import AsyncCategoryRepository
from src.abc.country.repo.country_repo import AsyncCountryRepository
from src.abc.repo.base_exceptions import UniqueViolationException, RepoException
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.dto.collects.collect import Collect
from src.dto.user.user import User


@dataclass
class CreateCollectDTO:
    name: str
    description: str
    target_amount: float
    category_name: str
    country_name: str
    image_uid: uuid.UUID
    user: User


class CreateCollectUC(BaseAsyncUseCase):
    def __init__(self,
                 collect_repo: IAsyncCollectRepository,
                 category_repo: AsyncCategoryRepository,
                 country_repo: AsyncCountryRepository,
                 collect_presenter: ICollectPresenter):
        self.collect_repo = collect_repo
        self.category_repo = category_repo
        self.country_repo = country_repo
        self.collect_presenter = collect_presenter

    async def execute(self, dto: CreateCollectDTO) -> Union[SuccessResponse, ErrorResponse]:
        # TODO file repo and check file exist

        category = await self.category_repo.get_list(name=dto.category_name)
        if not category:
            return ErrorResponse(f"Category {dto.category_name} not found", code=404)
        if len(category) > 1:
            return ErrorResponse(f"Category {dto.category_name} has more than one record", code=400)
        category = category[0]

        country = await self.country_repo.get_list(name=dto.country_name)
        if not country:
            return ErrorResponse(f"Country {dto.country_name} not found", code=404)
        if len(country) > 1:
            return ErrorResponse(f"Country {dto.country_name} has more than one record", code=400)

        country = country[0]

        collect_to_create = Collect(
            name=dto.name,
            description=dto.description,
            target_amount=dto.target_amount,
            current_amount=0,
            category=category,
            create_date=datetime.datetime.now(),
            status=False,
            country=country,
            image_uid=dto.image_uid,
            author=dto.user,
        )

        try:
            collect = await self.collect_repo.create(collect_to_create)
        except UniqueViolationException as e:
            return ErrorResponse(str(e), 404)
        except RepoException as e:
            return ErrorResponse(str(e), 500)
        collect = self.collect_presenter.get_collect_presentation(collect)
        return SuccessResponse(collect)

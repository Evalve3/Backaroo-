import uuid
from dataclasses import dataclass
from typing import Union

from src.abc.collect.presenters.collect_presenter import ICollectPresenter
from src.abc.collect.repo.collect_repo import AsyncCollectRepository
from src.abc.repo.base_exceptions import NotFoundException
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse


@dataclass
class GetCollectListDTO:
    collect_uid: uuid.UUID


class CreateCollectUC(BaseAsyncUseCase):
    def __init__(self,
                 collect_repo: AsyncCollectRepository,
                 collect_presenter: ICollectPresenter):
        self.collect_repo = collect_repo
        self.collect_presenter = collect_presenter

    async def execute(self, dto: GetCollectListDTO) -> Union[SuccessResponse, ErrorResponse]:

        try:
            collect = await self.collect_repo.get(dto.collect_uid)
        except NotFoundException as e:
            return ErrorResponse(str(e), code=404)

        collect = self.collect_presenter.get_collect_presentation(collect)

        return SuccessResponse(collect)

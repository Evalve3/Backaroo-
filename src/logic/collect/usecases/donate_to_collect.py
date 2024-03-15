import uuid
from _decimal import Decimal
from dataclasses import dataclass
from datetime import datetime
from typing import Union

from src.abc.collect.repo.collect_repo import IAsyncCollectRepository
from src.abc.collect.repo.donation_repo import IAsyncDonationRepository
from src.abc.repo.base_exceptions import NotFoundException, RepoException
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.dto.collects.donation import Donation, DonationStatus
from src.dto.user.user import User


@dataclass
class DonateToCollectDTO:
    collect_uid: uuid.UUID
    amount: Decimal
    user: User


class DonateToCollectUC(BaseAsyncUseCase):
    def __init__(self,
                 collect_repo: IAsyncCollectRepository,
                 donate_repo: IAsyncDonationRepository):
        self.collect_repo = collect_repo
        self.donate_repo = donate_repo

    async def execute(self, dto: DonateToCollectDTO) -> Union[SuccessResponse, ErrorResponse]:
        try:
            collect = await self.collect_repo.get(dto.collect_uid)
        except NotFoundException as e:
            return ErrorResponse(str(e), 404)

        try:
            donation_to_create = Donation(
                collect=collect,
                author=dto.user,
                amount=dto.amount,
                create_date=datetime.now(),
                status=DonationStatus.OK
            )
            donation = await self.donate_repo.create(donation_to_create)
        except RepoException as e:
            return ErrorResponse(str(e), 400)

        try:
            collect.current_amount += dto.amount
            await self.collect_repo.update(collect.uid, collect)
        except RepoException as e:
            return ErrorResponse(str(e), 400)

        return SuccessResponse(data='ok')

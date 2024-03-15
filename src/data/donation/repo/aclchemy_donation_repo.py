import uuid
from typing import Iterable, Optional

from src.abc.collect.repo.donation_repo import IAsyncDonationRepository
from src.data.donation.repo.alchemy_donation_mapper import DonationMapper
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.collects.donation import Donation


class AsyncDonationRepository(IAsyncDonationRepository, BaseSqlAlchemyAsyncRepository):

    async def get(self, uid: uuid.UUID) -> Optional[Donation]:
        pass

    async def get_list(self, **kwargs) -> Iterable[Donation]:
        pass

    async def create(self, other: Donation) -> Donation:
        donation = DonationMapper.to_model(other)
        self._session.add(donation)
        other.uid = donation.uid
        return other

    async def delete(self, uid: uuid.UUID) -> bool:
        pass

    async def update(self, uid: uuid.UUID, other: Donation) -> Donation:
        pass

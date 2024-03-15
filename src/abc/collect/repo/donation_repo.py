import uuid
from abc import ABC
from typing import Iterable, Optional

from src.abc.repo.base_repo import BaseAsyncRepository
from src.dto.collects.donation import Donation


class IAsyncDonationRepository(BaseAsyncRepository, ABC):

    async def get(self, uid: uuid.UUID) -> Optional[Donation]:
        pass

    async def get_list(self, **kwargs) -> Iterable[Donation]:
        pass

    async def create(self, other: Donation) -> Donation:
        pass

    async def delete(self, uid: uuid.UUID) -> bool:
        pass

    async def update(self, uid: uuid.UUID, other: Donation) -> Donation:
        pass

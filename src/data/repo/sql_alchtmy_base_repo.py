from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from src.abc.repo.base_repo import BaseAsyncRepository


class BaseSqlAlchemyAsyncRepository(BaseAsyncRepository, ABC):

    def __init__(self, session: AsyncSession):
        self._session = session

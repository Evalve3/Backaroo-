from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.repo.base_repo import BaseAsyncRepository


class BaseSqlAlchemyAsyncRepository(BaseAsyncRepository, ABC):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()

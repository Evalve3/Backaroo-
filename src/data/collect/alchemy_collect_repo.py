from typing import List
from uuid import UUID

from sqlalchemy import select, and_, desc, asc
from sqlalchemy.orm import joinedload

from models.collect.collect_model import CollectModel
from src.abc.collect.repo.collect_repo import IAsyncCollectRepository
from src.abc.repo.base_exceptions import UniqueViolationException, NotFoundException
from src.data.collect.aclhemy_collect_mapper import CollectMapper
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.collects.collect import Collect, CollectSortParameter


class AsyncCollectRepositoryAlchemy(IAsyncCollectRepository, BaseSqlAlchemyAsyncRepository):

    async def get(self, uid: UUID) -> Collect:
        collect = (await self._session.scalars(
            select(CollectModel).options(
                joinedload(CollectModel.country, CollectModel.author, CollectModel.category)).where(
                CollectModel.uid == uid))).first()
        collect_dto = CollectMapper.to_dto(collect)
        return collect_dto

    async def get_list(self, **kwargs) -> List[Collect]:
        query = select(CollectModel)
        conditions = [getattr(CollectModel, key) == value for key, value in kwargs.items() if
                      hasattr(CollectModel, key)]
        query = query.options(
                joinedload(CollectModel.country, CollectModel.author, CollectModel.category)).where(and_(*conditions))
        result = await self._session.execute(query)
        collects = result.scalars().all()
        return [CollectMapper.to_dto(collect) for collect in collects]

    async def get_page(self,
                       sort_by: CollectSortParameter,
                       on_page: int,
                       page: int,
                       sort_order: str = "desc",
                       **kwargs) -> List[Collect]:
        query = select(CollectModel)
        conditions = [getattr(CollectModel, key) == value for key, value in kwargs.items() if
                      hasattr(CollectModel, key)]
        query = query.options(
                joinedload(CollectModel.country, CollectModel.author, CollectModel.category)).where(and_(*conditions))

        if sort_order == "desc":
            query = query.order_by(desc(getattr(CollectModel, sort_by.value)))
        else:
            query = query.order_by(asc(getattr(CollectModel, sort_by.value)))

        query = query.limit(on_page).offset(on_page * (page - 1))

        result = await self._session.execute(query)
        collects = result.scalars().all()
        return [CollectMapper.to_dto(collect) for collect in collects]

    async def create(self, other: Collect) -> Collect:
        if (await self._session.scalars(select(CollectModel).where(CollectModel.uid == other.uid))).first():
            raise UniqueViolationException("Uid already exists")

        collect = CollectMapper.to_model(other)
        self._session.add(collect)
        collect_dto = CollectMapper.to_dto(collect)
        return collect_dto

    async def update(self, uid: UUID, collect: Collect) -> Collect:
        existing_collect = (await self._session.scalars(
            select(CollectModel).where(CollectModel.uid == uid))).first()

        if not existing_collect:
            raise NotFoundException("Collect not found")

        existing_collect.name = collect.name
        existing_collect.description = collect.description
        existing_collect.date = collect.date

        return CollectMapper.to_dto(existing_collect)

    async def delete(self, uid: UUID) -> bool:
        existing_collect = (await self._session.scalars(
            select(CollectModel).where(CollectModel.uid == uid))).first()

        if not existing_collect:
            raise NotFoundException("Collect not found")

        await self._session.delete(existing_collect)
        return True

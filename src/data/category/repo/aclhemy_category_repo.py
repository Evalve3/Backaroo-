from typing import List
from uuid import UUID

from sqlalchemy import select, and_

from models.category.category_model import CollectCategoryModel
from src.abc.collect_category.repo.category_repo import AsyncCategoryRepository
from src.abc.repo.base_exceptions import UniqueViolationException
from src.data.category.repo.aclhemy_category_mapper import CategoryMapper
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.category.category import CollectCategory


class CategoryRepoAlchemy(BaseSqlAlchemyAsyncRepository, AsyncCategoryRepository):

    async def get(self, uid: UUID) -> CollectCategory:
        category = (await self._session.scalars(
            select(CollectCategoryModel).where(CollectCategoryModel.uid == uid))).first()
        country_dto = CategoryMapper.to_dto(category)
        return country_dto

    async def get_list(self, **kwargs) -> List[CollectCategory]:
        query = select(CollectCategoryModel)
        conditions = [getattr(CollectCategoryModel, key) == value for key, value in kwargs.items() if
                      hasattr(CollectCategoryModel, key)]
        query = query.where(and_(*conditions))
        result = await self._session.execute(query)
        categorys = result.scalars().all()
        return [CategoryMapper.to_dto(category) for category in categorys]

    async def create(self, other: CollectCategory) -> CollectCategory:
        if (
        await self._session.scalars(select(CollectCategoryModel).where(CollectCategoryModel.uid == other.uid))).first():
            raise UniqueViolationException("Uid already exists")
        if (await self._session.scalars(
                select(CollectCategoryModel).where(CollectCategoryModel.name == other.name))).first():  # noqa
            raise UniqueViolationException("Name already exists")

        category = CategoryMapper.to_model(other)
        self._session.add(category)
        category_dto = CategoryMapper.to_dto(category)
        return category_dto

    async def update(self, uid: UUID, category: CollectCategory) -> CollectCategory:
        pass

    async def delete(self, uid: UUID) -> bool:
        pass

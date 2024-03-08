from typing import List
from uuid import UUID

from sqlalchemy import select, and_

from models.category.country_model import CountryModel
from src.abc.country.repo.country_repo import AsyncCountryRepository
from src.abc.repo.base_exceptions import UniqueViolationException
from src.data.country.repo.alchemy_country_mapper import CountryMapper
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.category.category import Country


class CountryRepoAlchemy(BaseSqlAlchemyAsyncRepository, AsyncCountryRepository):

    async def get(self, uid: UUID) -> Country:
        country = (await self._session.scalars(
            select(CountryModel).where(CountryModel.uid == uid))).first()
        country_dto = CountryMapper.to_dto(country)
        return country_dto

    async def get_list(self, **kwargs) -> List[Country]:
        query = select(CountryModel)
        conditions = [getattr(CountryModel, key) == value for key, value in kwargs.items() if hasattr(CountryModel, key)]
        query = query.where(and_(*conditions))
        result = await self._session.execute(query)
        countrys = result.scalars().all()
        return [CountryMapper.to_dto(country) for country in countrys]

    async def create(self, other: Country) -> Country:
        if (await self._session.scalars(select(CountryModel).where(CountryModel.uid == other.uid))).first():
            raise UniqueViolationException("Uid already exists")
        if (await self._session.scalars(select(CountryModel).where(CountryModel.name == other.name))).first():  # noqa
            raise UniqueViolationException("Country already exists")


        country = CountryMapper.to_model(other)
        self._session.add(country)
        country_dto = CountryMapper.to_dto(country)
        return country_dto

    async def update(self, uid: UUID, country: Country) -> Country:
        pass

    async def delete(self, uid: UUID) -> bool:
        pass

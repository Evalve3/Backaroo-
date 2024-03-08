import asyncio
from typing import List, Tuple
from uuid import UUID

from sqlalchemy import select, and_
from sqlalchemy.orm import joinedload

from models.category.country_model import CountryModel
from src.abc.repo.base_exceptions import UniqueViolationException, NotFoundException
from src.abc.user.repo.user_repo import AsyncUserRepository
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.data.user.repo.aclhemy_user_mapper import UserMapper
from src.dto.user.user import User
from models.user.user_model import UserModel


class UserRepoAlchemy(BaseSqlAlchemyAsyncRepository, AsyncUserRepository):

    async def get(self, uid: UUID) -> User:
        user = (await self._session.scalars(
            select(UserModel).options(joinedload(UserModel.country)).where(UserModel.uid == uid))).first()
        user_dto = UserMapper.to_dto(user)
        return user_dto

    async def get_list(self, **kwargs) -> List[User]:
        query = select(UserModel)
        conditions = [getattr(UserModel, key) == value for key, value in kwargs.items() if hasattr(UserModel, key)]
        query = query.options(joinedload(UserModel.country)).where(and_(*conditions))
        result = await self._session.execute(query)
        users = result.scalars().all()
        return [UserMapper.to_dto(user) for user in users]

    async def create(self, other: User) -> User:
        if (await self._session.scalars(select(UserModel).where(UserModel.uid == other.uid))).first():
            raise UniqueViolationException("Uid already exists")
        if (await self._session.scalars(select(UserModel).where(UserModel.username == other.username))).first():  # noqa
            raise UniqueViolationException("Username already exists")
        if (await self._session.scalars(select(UserModel).where(UserModel.email == other.email))).first():  # noqa
            raise UniqueViolationException("Email already exists")

        user = UserMapper.to_model(other)
        self._session.add(user)
        user_dto = UserMapper.to_dto(user)
        return user_dto

    async def update(self, uid: UUID, user: User) -> User:
        # Get the existing user
        existing_user = (await self._session.scalars(
            select(UserModel).options(joinedload(UserModel.country)).where(UserModel.uid == uid))).first()


        # If user does not exist, raise an exception
        if not existing_user:
            raise NotFoundException("User not found")

        country = None
        if user.country:
            country = (await self._session.scalars(
                select(CountryModel).where(CountryModel.uid == user.country.uid))).first()

        # Update the fields of the existing user
        existing_user.username = user.username
        existing_user.first_name = user.first_name
        existing_user.last_name = user.last_name
        existing_user.date_birth = user.date_birth
        existing_user.email = user.email
        existing_user.avatar_id = user.avatar_id
        existing_user.additional_info = user.additional_info
        existing_user.sex = user.sex
        existing_user.country = country

        # Return the updated user
        return UserMapper.to_dto(existing_user)

    async def delete(self, uid: UUID) -> bool:
        pass

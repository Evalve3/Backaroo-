from abc import ABC
from typing import Iterable
from uuid import UUID

from sqlalchemy import select

from models.file.file_model import FileModel
from src.abc.file.file_repo import AsyncFileRepositoryABC
from src.data.file.repo.file_mapper import FileMapper
from src.data.repo.sql_alchtmy_base_repo import BaseSqlAlchemyAsyncRepository
from src.dto.base_dto import BaseEntity
from src.dto.file.file_dto import File


class AsyncFileRepository(AsyncFileRepositoryABC, BaseSqlAlchemyAsyncRepository):

    async def get_list(self, **kwargs) -> Iterable[BaseEntity]:
        pass

    async def update(self, uid: str, other: BaseEntity) -> BaseEntity:
        pass

    async def create(self, file: File) -> File:
        user = FileMapper.to_model(file)
        self._session.add(user)
        user_dto = FileMapper.to_dto(user)
        return user_dto

    async def get(self, uid: UUID) -> File:
        file = (await self._session.scalars(
            select(FileModel).where(FileModel.uid == uid))).first()
        file_dto = FileMapper.to_dto(file)
        return file_dto

    async def delete(self, uid: UUID) -> bool:
        pass

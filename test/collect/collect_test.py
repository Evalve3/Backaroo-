import datetime

import pytest
from uuid import uuid4

from models.session import get_session
from src.data.collect.alchemy_collect_repo import AsyncCollectRepositoryAlchemy
from src.dto.category.category import CollectCategory, Country
from src.dto.collects.collect import Collect, CollectSortParameter
from src.abc.repo.base_exceptions import UniqueViolationException, NotFoundException
from src.dto.user.user import User


@pytest.fixture
def session():
    return get_session()


@pytest.fixture
def collect():
    return Collect(uid=uuid4(),
                   name="Test Collect",
                   description="Test Description",
                   create_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d"),
                   target_amount=1000,
                   current_amount=0,
                   category=CollectCategory(uid=uuid4(), name="Test Category"),
                   status=False,
                   country=Country(uid=uuid4(), name="Test Country"),
                   image_uid=uuid4(),
                   author=User(uid=uuid4(), username="Test User",
                               first_name="Test", last_name="User", email="asd@asd.com", date_birth=datetime.date(1990, 1, 1)))

@pytest.mark.asyncio
async def test_create_collect_when_not_exists(collect, session):
    async for s in session:
        repo = AsyncCollectRepositoryAlchemy(session=s)
        async with s.begin():
            result = await repo.create(collect)
            assert result == collect

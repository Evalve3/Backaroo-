from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import settings

# create async engine for interaction with database
engine = create_async_engine(
    settings.REAL_DATABASE_URL,
    future=True,
    echo=True,
    # expire_on_commit=False
)

# create session for the interaction with database
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

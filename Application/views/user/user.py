import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Application.views.user.schemas import UserCreate
from src.core.usecase.user.create_user import CreateUserUC
from src.data.repo.user.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from src.models.session import async_session, get_session

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/create')
async def create_user(body: UserCreate, session: AsyncSession = Depends(get_session)):
    repo = UserRepoAlchemy(
        session=session
    )
    user_to_create = User(first_name=body.first_name,
                          last_name=body.last_name,
                          username=body.username,
                          date_birth=body.date_birth,
                          email=body.email,
                          hashed_password=body.password)
    uc = CreateUserUC(user_repo=repo)
    res = await uc.execute(user=user_to_create)
    return res

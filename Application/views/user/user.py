import datetime

from fastapi import APIRouter

from src.data.repo.user.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from src.models.session import async_session, get_db

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/create')
async def create_user():
    session = async_session()
    repo = UserRepoAlchemy(
        session= session
    )

    async with repo:
        user = await repo.create(
            other=User(
                username='tsesst',
                first_name='tessst',
                last_name='tessst',
                date_birth=datetime.datetime.now(),
                email='qwses',
                avatar='qswes',
                is_active=True,
                hashed_password='qwe'

            )
        )

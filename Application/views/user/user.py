from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from Application.security.jwt_token import create_access_token
from Application.views.user.schemas import UserCreate, ShowUser, Token
from Application.views.auth import authenticate_user, get_current_user_from_token
from src.abc.usecase.base_usecase import ErrorResponse
from src.logic.user.usecases.create_user import CreateUserUC
from src.data.user.repo.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from models.session import get_session
from hashlib import sha256

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/create')
async def create_user(body: UserCreate,
                      session: AsyncSession = Depends(get_session)) -> ShowUser:
    hashed_password = sha256(body.password.encode()).hexdigest()
    user_to_create = User(first_name=body.first_name,
                          last_name=body.last_name,
                          username=body.username,
                          date_birth=body.date_birth,
                          email=body.email,
                          hashed_password=hashed_password)
    async with session.begin():
        user_repo = UserRepoAlchemy(session=session)
        create_user_case = CreateUserUC(user_repo=user_repo)
        res = await create_user_case.execute(user=user_to_create)

        if isinstance(res, ErrorResponse):  # очень важно проверять тип ответа внутри контекстного менеджера
            # чтобы транзакция откатилась если произошла ошибка
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )

    user = res.data
    show_user = ShowUser(uid=user.uid,
                         first_name=user.first_name,
                         last_name=user.last_name,
                         email=user.email,
                         is_active=user.is_active)
    return show_user


@user_router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 session: AsyncSession = Depends(get_session)) -> Token:
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": str(user.uid), "username": user.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@user_router.get('/me', response_model=ShowUser)
async def read_users_me(current_user: User = Depends(get_current_user_from_token)) -> ShowUser:
    res = ShowUser(uid=current_user.uid,
                   first_name=current_user.first_name,
                   last_name=current_user.last_name,
                   email=current_user.email,
                   is_active=current_user.is_active,
                   country=current_user.country.name if current_user.country else None,
                   avatar_file_id=current_user.avatar_id if current_user.avatar_id else None
                   )
    return res

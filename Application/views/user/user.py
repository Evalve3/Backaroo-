from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from Application.security.jwt_token import create_access_token
from Application.views.user.schemas import UserCreate, ShowUser, Token
from Application.views.auth import authenticate_user, get_current_user_from_token
from src.core.usecase.user.create_user import CreateUserUC
from src.data.repo.user.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from src.models.session import get_session
from hashlib import sha256

user_router = APIRouter(prefix='/user', tags=['user'])


async def get_create_user_uc(session: AsyncSession = Depends(get_session)) -> CreateUserUC:
    repo = UserRepoAlchemy(
        session=session
    )
    return CreateUserUC(user_repo=repo)


@user_router.post('/create')
async def create_user(body: UserCreate,
                      create_user_case: CreateUserUC = Depends(get_create_user_uc)) -> ShowUser:
    hashed_password = sha256(body.password.encode()).hexdigest()
    user_to_create = User(first_name=body.first_name,
                          last_name=body.last_name,
                          username=body.username,
                          date_birth=body.date_birth,
                          email=body.email,
                          hashed_password=hashed_password)
    res = await create_user_case.execute(user=user_to_create)
    show_user = ShowUser(uid=res.uid,
                         first_name=res.first_name,
                         last_name=res.last_name,
                         email=res.email,
                         is_active=res.is_active)
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
        data={"sub": user.uid, "username": user.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@user_router.get('/me', response_model=ShowUser)
async def read_users_me(current_user: User = Depends(get_current_user_from_token)) -> ShowUser:
    res = ShowUser(uid=current_user.uid,
                   first_name=current_user.first_name,
                   last_name=current_user.last_name,
                   email=current_user.email,
                   is_active=current_user.is_active)
    return res

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from Application.security.jwt_token import create_access_token
from Application.views.user.schemas import UserCreateSchema, ShowUserSchema, Token, UserEditSchema
from Application.views.auth import authenticate_user, get_current_user_from_token
from src.abc.usecase.base_usecase import ErrorResponse
from src.data.country.repo.alchemy_country_repo import CountryRepoAlchemy
from Application.views.user.presenters.user_presenter import UserPresenter
from src.logic.user.usecases.create_user import CreateUserUC, CreateUserDTO
from src.data.user.repo.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from models.session import get_session
from hashlib import sha256

from src.logic.user.usecases.edit_user import EditUserUC, EditUserDTO

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post('/')
async def create_user(body: UserCreateSchema,
                      session: AsyncSession = Depends(get_session)) -> ShowUserSchema:
    """
    Создание пользователя
    """
    hashed_password = sha256(body.password.encode()).hexdigest()
    user_to_create = User(first_name=body.first_name,
                          last_name=body.last_name,
                          username=body.username,
                          date_birth=body.date_birth,
                          email=body.email,
                          hashed_password=hashed_password)
    async with session.begin():
        user_repo = UserRepoAlchemy(session=session)
        presenter = UserPresenter()
        create_user_case = CreateUserUC(user_repo=user_repo, user_presenter=presenter)
        dto = CreateUserDTO(user=user_to_create)
        res = await create_user_case.execute(dto=dto)

        if isinstance(res, ErrorResponse):  # очень важно проверять тип ответа внутри контекстного менеджера
            # чтобы транзакция откатилась если произошла ошибка
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )

        return res.data


@user_router.put('/')
async def edit_user(body: UserEditSchema,
                    session: AsyncSession = Depends(get_session),
                    current_user: User = Depends(get_current_user_from_token)
                    ) -> ShowUserSchema:
    """
    Редактирование пользователя
    """
    async with session.begin():
        user_repo = UserRepoAlchemy(session=session)
        presenter = UserPresenter()
        country_repo = CountryRepoAlchemy(session=session)
        edit_user_case = EditUserUC(user_repo=user_repo, user_presenter=presenter, country_repo=country_repo)
        dto = EditUserDTO(user_uid_to_edit=current_user.uid,
                          username=body.username,
                          first_name=body.first_name,
                          last_name=body.last_name,
                          date_birth=body.date_birth,
                          email=body.email,
                          avatar_id=body.avatar_id,
                          additional_info=body.additional_info,
                          sex=body.sex,
                          country=body.country)
        res = await edit_user_case.execute(dto=dto)
        if isinstance(res, ErrorResponse):
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )

        return res.data


@user_router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 session: AsyncSession = Depends(get_session)) -> Token:
    """
    Получение токена
    """
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": str(user.uid), "username": user.username, "avatar_file_id": str(user.avatar_id)},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@user_router.get('/me', response_model=ShowUserSchema)
async def read_users_me(current_user: User = Depends(get_current_user_from_token)) -> ShowUserSchema:
    """
    Получение информации о текущем пользователе
    """
    presenter = UserPresenter()
    res = presenter.get_user_presentation(current_user)
    return res

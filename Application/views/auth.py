from hashlib import sha256
from typing import Union
from uuid import UUID

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import settings
from src.data.repo.user.achemy_user_repo import UserRepoAlchemy
from src.dto.user.user import User
from src.models.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


async def get_current_user_from_token(
        token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)
) -> User:
    repo = UserRepoAlchemy(
        session=session
    )

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        uid: UUID = payload.get("sub")
        if uid is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await repo.get(uid)
    if user is None:
        raise credentials_exception
    return user


async def authenticate_user(username: str, password: str, session: AsyncSession) -> Union[User, None]:
    repo = UserRepoAlchemy(
        session=session
    )
    users = await repo.get_list(username=username)
    if not users:
        return
    if len(users) > 1:
        return  # should not happen
    user = users[0]
    if sha256(password.encode()).hexdigest() != user.hashed_password:
        return
    return user

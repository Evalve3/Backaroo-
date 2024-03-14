import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class UserCreateSchema(BaseModel):
    first_name: str
    username: str
    last_name: str
    email: EmailStr
    password: str
    date_birth: datetime.date = Field()


class UserEditSchema(BaseModel):
    username: str = None
    first_name: str = None
    last_name: str = None
    date_birth: datetime.date = None
    email: str = None
    avatar_id: Optional[uuid.UUID] = None
    additional_info: Optional[str] = None
    sex: Optional[bool] = None
    country: Optional[str] = None


class UserPreviewSchema(BaseModel):
    uid: uuid.UUID
    avatar_file_id: Optional[uuid.UUID] = None
    username: str


class ShowUserSchema(BaseModel):
    uid: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    country: Optional[str] = None
    avatar_file_id: Optional[uuid.UUID] = None
    username: str
    date_birth: datetime.date
    additional_info: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str

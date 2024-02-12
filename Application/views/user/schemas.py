import re
import datetime
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator, Field

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class UserCreate(BaseModel):
    first_name: str
    username: str
    last_name: str
    email: EmailStr
    password: str
    date_birth: datetime.date = Field()


class ShowUser(BaseModel):
    uid: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool


class Token(BaseModel):
    access_token: str
    token_type: str

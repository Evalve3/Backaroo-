import base64
import uuid

from fastapi import APIRouter, Depends, UploadFile, File as Fastapi_file
from sqlalchemy.ext.asyncio import AsyncSession

from Application.views.auth import get_current_user_from_token
from models.session import get_session
from src.data.file.repo.file_repo import AsyncFileRepository
from src.dto.file.file_dto import File
from src.dto.user.user import User

file_router = APIRouter(prefix='/file', tags=['file'])


@file_router.post('/')
async def create_file(session: AsyncSession = Depends(get_session),
                      file: UploadFile = Fastapi_file(...),
                      current_user: User = Depends(get_current_user_from_token)):
    file_data = file.file.read()
    file_to_create = File(name=file.filename, data=file_data)
    file_repo = AsyncFileRepository(session=session)
    async with session.begin():
        created_file = await file_repo.create(file=file_to_create)

    return {"filename": file.filename}


@file_router.get('/')
async def get_file(file_id: uuid.UUID, session: AsyncSession = Depends(get_session),
                   current_user: User = Depends(get_current_user_from_token),
                   ):
    file_repo = AsyncFileRepository(session=session)
    async with session.begin():
        created_file = await file_repo.get(uid=file_id)
    encoded_file_data = base64.b64encode(created_file.data).decode('utf-8')

    return {"file": encoded_file_data}

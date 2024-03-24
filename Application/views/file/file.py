import base64
import tempfile
import uuid

from fastapi import APIRouter, Depends, UploadFile, File as Fastapi_file
from sqlalchemy.ext.asyncio import AsyncSession

from Application.views.auth import get_current_user_from_token
from models.session import get_session
from src.data.file.repo.file_repo import AsyncFileRepository
from src.dto.file.file_dto import File
from src.dto.user.user import User
from starlette.responses import FileResponse

file_router = APIRouter(prefix='/file', tags=['file'])


@file_router.post('/')
async def create_file(session: AsyncSession = Depends(get_session),
                      file: UploadFile = Fastapi_file(...),
                      current_user: User = Depends(get_current_user_from_token)):
    # TODO usecase
    file_data = file.file.read()
    file_to_create = File(name=file.filename, data=file_data)
    file_repo = AsyncFileRepository(session=session)
    async with session.begin():
        created_file = await file_repo.create(file=file_to_create)

    return {"uid": created_file.uid}


@file_router.get('/{file_id}')
async def get_file(file_id: uuid.UUID, session: AsyncSession = Depends(get_session)):
    # TODO usecase
    file_repo = AsyncFileRepository(session=session)
    async with session.begin():
        created_file = await file_repo.get(uid=file_id)

    # Create a temporary file and write the data to it
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(created_file.data)
    temp_file.close()

    # Return a FileResponse that reads from the temporary file
    # The media_type is set to 'application/octet-stream' to handle any type of file
    # The filename in the Content-Disposition header is set to the original file name
    return FileResponse(temp_file.name, media_type="image/png",
                        filename=created_file.name, content_disposition_type='inline')

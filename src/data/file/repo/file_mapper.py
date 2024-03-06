import base64

from models.file.file_model import FileModel
from src.dto.file.file_dto import File



class FileMapper:

    @staticmethod
    def to_dto(file: FileModel) -> File:
        return File(
            uid=file.uid,
            name=file.name,
            data=file.data
        )

    @staticmethod
    def to_model(file: File) -> FileModel:
        return FileModel(
            uid=file.uid,
            name=file.name,
            data=file.data
        )

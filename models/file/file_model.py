from sqlalchemy import Column, String, LargeBinary, UUID
from models.db_init import Base
import uuid


class FileModel(Base):
    __tablename__ = "files"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)

    def dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
        }

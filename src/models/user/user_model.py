import uuid

from sqlalchemy import Boolean, TIMESTAMP, Date
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from src.models.db_init import Base


class UserModel(Base):
    __tablename__ = "users"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    avatar = Column(String, nullable=True)
    date_birth = Column(Date, nullable=False)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)

    def dict(self):
        return {
            "uid": str(self.uid),
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "avatar": self.avatar,
            "date_birth": self.date_birth,
            "is_active": self.is_active,
            "hashed_password": self.hashed_password,
        }

import uuid

from sqlalchemy import Boolean, Date, func, ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.category.country_model import CountryModel
from models.db_init import Base


class UserModel(Base):
    __tablename__ = "users"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # id
    username = Column(String, nullable=False, unique=True)  # login
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    avatar = Column(String, nullable=True)  # url to avatar img
    date_birth = Column(Date, nullable=False)
    is_active = Column(Boolean(), default=True)  # ban / unban
    hashed_password = Column(String, nullable=False)
    profile_status = Column(String, nullable=True)  # status (rcf - need verification, active, ban)
    profile_background = Column(String, nullable=True)  # url to background img
    additional_info = Column(String, nullable=True)  # additional info
    sex = Column(Boolean, nullable=True)
    adult_content = Column(Boolean, nullable=True)  # adult content status
    registration_date = Column(Date, server_default=func.now())  # registration date
    country_id = Column(UUID(as_uuid=True), ForeignKey('countries.uid'))  # foreign key to country
    country = relationship(CountryModel)  # relationship to CountryModel

    def dict(self):
        return {
            "uid": self.uid,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "avatar": self.avatar,
            "date_birth": self.date_birth,
            "is_active": self.is_active,
            "hashed_password": self.hashed_password,
            "profile_status": self.profile_status,
            "profile_background": self.profile_background,
            "additional_info": self.additional_info,
            "sex": self.sex,
            "adult_content": self.adult_content,
            "registration_date": self.registration_date,
            "country_id": self.country_id,
        }

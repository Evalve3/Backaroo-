import uuid

from sqlalchemy import Boolean, Date, func, ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.collect.collect_model import CollectModel
from models.db_init import Base
from models.user.user_model import UserModel


class CommentModel(Base):
    __tablename__ = "comments"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # id
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.uid'), nullable=False)
    author = relationship(UserModel)
    text = Column(String, nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())
    collect_id = Column(UUID(as_uuid=True), ForeignKey('collects.uid'), nullable=False)
    collect = relationship(CollectModel)

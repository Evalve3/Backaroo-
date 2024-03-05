import uuid

from sqlalchemy import Date, func, ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.collect.collect_model import CollectModel
from models.db_init import Base
from models.user.user_model import UserModel


class QuestionModel(Base):
    __tablename__ = "questions"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # id
    text = Column(String, nullable=False)
    collect_id = Column(UUID(as_uuid=True), ForeignKey('collects.uid'), nullable=False)
    collect = relationship(CollectModel)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.uid'), nullable=False)
    author = relationship(UserModel, back_populates='questions')
    create_date = Column(Date, nullable=False, server_default=func.now())


class QuestionAnswerModel(Base):
    __tablename__ = "question_answers"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # id
    question_id = Column(UUID(as_uuid=True), ForeignKey('questions.uid'), nullable=False)
    question = relationship(QuestionModel, back_populates='answers')
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.uid'), nullable=False)
    author = relationship(UserModel)
    text = Column(String, nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())

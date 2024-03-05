import uuid

from sqlalchemy import Date, func, ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.collect.collect_model import CollectModel
from models.db_init import Base


class NewsModel(Base):
    __tablename__ = "news"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # id
    name = Column(String, nullable=False)
    text = Column(String, nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())
    collect_id = Column(UUID(as_uuid=True), ForeignKey('collects.uid'), nullable=False)
    collect = relationship(CollectModel)

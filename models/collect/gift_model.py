import uuid

from sqlalchemy import Column, UUID, String


from models.db_init import Base


class GiftModel(Base):
    __tablename__ = "gifts"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)

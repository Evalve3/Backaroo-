import uuid

from sqlalchemy import Column, UUID, String

from models.db_init import Base


class CollectCategoryModel(Base):
    __tablename__ = "categories"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)

    def dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
        }


class SupportCategoryModel(Base):
    __tablename__ = "support_categories"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)

    def dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
        }

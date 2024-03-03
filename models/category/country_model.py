import uuid

from sqlalchemy import Column, UUID, String

from models.db_init import Base


class CountryModel(Base):
    __tablename__ = "countries"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    icon_url = Column(String, nullable=True)

    def dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "icon_url": self.icon_url,
        }

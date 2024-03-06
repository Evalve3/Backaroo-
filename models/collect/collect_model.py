import uuid

from sqlalchemy import Column, UUID, String, Numeric, Date, func, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models.category.category_model import CollectCategoryModel
from models.category.country_model import CountryModel
from models.db_init import Base
from models.file.file_model import FileModel


class CollectModel(Base):
    __tablename__ = "collects"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    target_amount = Column(Numeric, nullable=False)
    current_amount = Column(Numeric, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.uid'), nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())
    category = relationship(CollectCategoryModel)
    status = Column(Boolean, nullable=False)
    country_id = Column(UUID(as_uuid=True), ForeignKey('countries.uid'), nullable=False)
    country = relationship(CountryModel)
    image_id = Column(UUID(as_uuid=True), ForeignKey('files.uid'), nullable=True)
    image = relationship(FileModel)

    def dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "description": self.description,
            "target_amount": self.target_amount,
            "current_amount": self.current_amount,
            "category_id": self.category_id,
            "create_date": self.create_date,
            "status": self.status,
            "country_id": self.country_id
        }

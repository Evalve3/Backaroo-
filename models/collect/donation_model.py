import uuid

from sqlalchemy import Column, UUID, Numeric, Date, func, ForeignKey, Enum, String
from sqlalchemy.orm import relationship

from models.collect.collect_model import CollectModel
from models.db_init import Base
from models.user.user_model import UserModel


class DonationModel(Base):
    __tablename__ = "donations"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collect_id = Column(UUID(as_uuid=True), ForeignKey('collects.uid'), nullable=False)
    collect = relationship(CollectModel)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.uid'), nullable=False)
    author = relationship(UserModel)
    amount = Column(Numeric, nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())
    status = Column(String, nullable=False)  # CNCLD', 'FAIL', 'RCVD', 'OK'

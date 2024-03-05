import uuid

from sqlalchemy import ForeignKey, UUID, Column, Date, func, Text, Boolean
from sqlalchemy.orm import relationship

from models.collect.collect_model import CollectModel
from models.db_init import Base
from models.user.user_model import UserModel


class SubscribeNotificationModel(Base):
    __tablename__ = "subscribe_notifications"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collect_id = Column(UUID(as_uuid=True), ForeignKey('collects.uid'), nullable=False)
    collect = relationship(CollectModel)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.uid'), nullable=False)
    user = relationship(UserModel)
    create_date = Column(Date, nullable=False, server_default=func.now())


class NotificationModel(Base):
    __tablename__ = "notifications"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subscribe_id = Column(UUID(as_uuid=True), ForeignKey('subscribe_notifications.uid'), nullable=False)
    subscribe = relationship(SubscribeNotificationModel)
    text = Column(Text, nullable=False)
    create_date = Column(Date, nullable=False, server_default=func.now())
    status = Column(Boolean, nullable=False)

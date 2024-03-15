import uuid
from _decimal import Decimal
from datetime import datetime
from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field

from Application.views.user.schemas import UserPreviewSchema
from src.dto.collects.collect import CollectSortParameter, SortOrder


class ShowCollectSchema(BaseModel):
    name: str
    description: str
    target_amount: float
    current_amount: float
    category: str
    create_date: datetime
    status: bool
    country: str
    image_file_id: uuid.UUID
    author: UserPreviewSchema
    uid: uuid.UUID


class ShowCollectsSchema(BaseModel):
    collects: list[ShowCollectSchema]
    count: int
    page: int
    on_page: int


class CreateCollectSchema(BaseModel):
    name: str
    description: str
    target_amount: float = Field(..., ge=100, le=99999999)
    category_name: str
    country_name: str
    image_file_id: uuid.UUID


class CollectPageParams(BaseModel):
    page: int = Query(1, ge=1)
    on_page: int = Query(10, ge=1, le=100)
    category_name: Optional[str] = Query(None)
    country_name: Optional[str] = Query(None)
    sort_by: CollectSortParameter = Query(CollectSortParameter.NAME)
    sort_order: SortOrder = Query(SortOrder.asc)


class CreateMockDonateSchema(BaseModel):
    collect_uid: uuid.UUID
    amount: Decimal

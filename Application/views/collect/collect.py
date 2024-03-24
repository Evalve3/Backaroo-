import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from Application.views.auth import get_current_user_from_token
from Application.views.collect.presenters.collect_presenter import CollectPresenter
from Application.views.collect.schemas import CreateCollectSchema, ShowCollectSchema, ShowCollectsSchema, \
    CollectPageParams, CreateMockDonateSchema
from models.session import get_session
from src.abc.usecase.base_usecase import ErrorResponse
from src.data.category.repo.aclhemy_category_repo import CategoryRepoAlchemy
from src.data.collect.repo.alchemy_collect_repo import AsyncCollectRepositoryAlchemy
from src.data.country.repo.alchemy_country_repo import CountryRepoAlchemy
from src.data.donation.repo.aclchemy_donation_repo import AsyncDonationRepository
from src.data.file.repo.file_repo import AsyncFileRepository
from src.dto.user.user import User
from src.logic.collect.usecases.create_collect import CreateCollectUC, CreateCollectDTO
from src.logic.collect.usecases.donate_to_collect import DonateToCollectUC, DonateToCollectDTO
from src.logic.collect.usecases.get_collect import GetCollectUC, GetCollectDTO
from src.logic.collect.usecases.get_collect_list import GetCollectListUC, GetCollectListDTO

collect_router = APIRouter(prefix='/collect', tags=['collect'])


@collect_router.post('/')
async def create_collect(body: CreateCollectSchema,
                         session: AsyncSession = Depends(get_session),
                         current_user: User = Depends(get_current_user_from_token),
                         ) -> ShowCollectSchema:
    """
    (привет Катя)
    Создание сбора
    """
    async with session.begin():
        category_repo = CategoryRepoAlchemy(session=session)
        collect_repo = AsyncCollectRepositoryAlchemy(session=session)
        country_repo = CountryRepoAlchemy(session=session)
        file_repo = AsyncFileRepository(session=session)
        collect_presenter = CollectPresenter()
        uc = CreateCollectUC(collect_repo=collect_repo, category_repo=category_repo,
                             country_repo=country_repo, collect_presenter=collect_presenter,
                             file_repo=file_repo)
        dto = CreateCollectDTO(
            name=body.name,
            description=body.description,
            target_amount=body.target_amount,
            category_name=body.category_name,
            country_name=body.country_name,
            image_uid=body.image_file_id,
            user=current_user
        )
        res = await uc.execute(dto=dto)
        if isinstance(res, ErrorResponse):
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )
        return res.data


@collect_router.get('/{collect_uid}')
async def get_collect(collect_uid: uuid.UUID,
                      session: AsyncSession = Depends(get_session)) -> ShowCollectSchema:
    """
    Получение информации о сборе
    """
    async with session.begin():
        collect_repo = AsyncCollectRepositoryAlchemy(session=session)
        collect_presenter = CollectPresenter()
        uc = GetCollectUC(collect_repo=collect_repo, collect_presenter=collect_presenter)
        dto = GetCollectDTO(collect_uid=collect_uid)
        res = await uc.execute(dto=dto)
        if isinstance(res, ErrorResponse):
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )
        return res.data


@collect_router.get('/list/page')
async def get_collect_page(params: CollectPageParams = Depends(),
                           session: AsyncSession = Depends(get_session),
                           ) -> ShowCollectsSchema:
    """
    Получение страницы сборов
    """
    async with session.begin():
        collect_repo = AsyncCollectRepositoryAlchemy(session=session)
        collect_presenter = CollectPresenter()
        category_repo = CategoryRepoAlchemy(session=session)
        country_repo = CountryRepoAlchemy(session=session)
        uc = GetCollectListUC(collect_repo=collect_repo, collect_presenter=collect_presenter,
                              category_repo=category_repo, country_repo=country_repo)
        dto = GetCollectListDTO(page=params.page, on_page=params.on_page,
                                category_name=params.category_name,
                                country_name=params.country_name,
                                sort_by=params.sort_by,
                                sort_order=params.sort_order,
                                text_to_search=params.search)
        res = await uc.execute(dto=dto)
        if isinstance(res, ErrorResponse):
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )
        return res.data


@collect_router.post('/mock/donate')
async def mock_donate(
        body: CreateMockDonateSchema,
        session: AsyncSession = Depends(get_session),
        current_user: User = Depends(get_current_user_from_token)) -> str:
    """
    Мок для совершения доната
    """
    async with session.begin():
        collect_repo = AsyncCollectRepositoryAlchemy(session=session)
        donation_repo = AsyncDonationRepository(session=session)
        uc = DonateToCollectUC(collect_repo=collect_repo, donate_repo=donation_repo)
        dto = DonateToCollectDTO(
            collect_uid=body.collect_uid,
            amount=body.amount,
            user=current_user
        )
        res = await uc.execute(dto=dto)
        if isinstance(res, ErrorResponse):
            raise HTTPException(
                status_code=res.code,
                detail=res.error
            )
        return res.data

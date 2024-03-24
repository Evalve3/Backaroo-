from dataclasses import dataclass
from typing import Union, Optional

from src.abc.collect.presenters.collect_presenter import ICollectPresenter
from src.abc.collect.repo.collect_repo import IAsyncCollectRepository
from src.abc.collect_category.repo.category_repo import AsyncCategoryRepository
from src.abc.country.repo.country_repo import AsyncCountryRepository
from src.abc.usecase.base_usecase import BaseAsyncUseCase, SuccessResponse, ErrorResponse
from src.dto.collects.collect import CollectSortParameter, SortOrder


@dataclass
class GetCollectListDTO:
    category_name: Optional[str] = None
    country_name: Optional[str] = None
    sort_by: CollectSortParameter = CollectSortParameter.NAME
    on_page: int = 10
    page: int = 1
    sort_order: SortOrder = SortOrder.desc
    text_to_search: Optional[str] = None


class GetCollectListUC(BaseAsyncUseCase):
    def __init__(self,
                 collect_repo: IAsyncCollectRepository,
                 category_repo: AsyncCategoryRepository,
                 country_repo: AsyncCountryRepository,
                 collect_presenter: ICollectPresenter):
        self.collect_repo = collect_repo
        self.category_repo = category_repo
        self.country_repo = country_repo
        self.collect_presenter = collect_presenter

    async def execute(self, dto: GetCollectListDTO) -> Union[SuccessResponse, ErrorResponse]:

        category = None
        if dto.category_name is not None:
            category = await self.category_repo.get_list(name=dto.category_name)
            if not category:
                return ErrorResponse(f"Category {dto.category_name} not found", code=404)
            if len(category) > 1:
                return ErrorResponse(f"Category {dto.category_name} has more than one record", code=400)
            category = category[0]

        country = None
        if dto.country_name is not None:
            country = await self.country_repo.get_list(name=dto.country_name)
            if not country:
                return ErrorResponse(f"Country {dto.country_name} not found", code=404)
            if len(country) > 1:
                return ErrorResponse(f"Country {dto.country_name} has more than one record", code=400)

            country = country[0]

        if category and country:
            if dto.sort_by in (CollectSortParameter.COUNTRY, CollectSortParameter.CATEGORY):
                return ErrorResponse(f"Sort by {dto.sort_by} is not allowed for category and country", code=400)
            collects = await self.collect_repo.get_page(category=category,
                                                        text_to_search=dto.text_to_search,
                                                        sort_order=dto.sort_order,
                                                        country=country,
                                                        sort_by=dto.sort_by,
                                                        on_page=dto.on_page,
                                                        page=dto.page)
            total = await self.collect_repo.get_count(text_to_search=dto.text_to_search,
                                                      category=category,
                                                      country=country)
        elif category and not country:
            if dto.sort_by == CollectSortParameter.CATEGORY:
                return ErrorResponse(f"Sort by {dto.sort_by} is not allowed for category", code=400)
            collects = await self.collect_repo.get_page(category=category,
                                                        sort_order=dto.sort_order,
                                                        text_to_search=dto.text_to_search,
                                                        sort_by=dto.sort_by,
                                                        on_page=dto.on_page,
                                                        page=dto.page)
            total = await self.collect_repo.get_count(text_to_search=dto.text_to_search,
                                                      category=category)
        elif not category and country:
            if dto.sort_by == CollectSortParameter.COUNTRY:
                return ErrorResponse(f"Sort by {dto.sort_by} is not allowed for country", code=400)
            collects = await self.collect_repo.get_page(country=country,
                                                        sort_order=dto.sort_order,
                                                        text_to_search=dto.text_to_search,
                                                        sort_by=dto.sort_by,
                                                        on_page=dto.on_page,
                                                        page=dto.page)
            total = await self.collect_repo.get_count(text_to_search=dto.text_to_search,
                                                      country=country)
        else:
            collects = await self.collect_repo.get_page(sort_by=dto.sort_by,
                                                        sort_order=dto.sort_order,
                                                        text_to_search=dto.text_to_search,
                                                        on_page=dto.on_page,
                                                        page=dto.page)
            total = await self.collect_repo.get_count(text_to_search=dto.text_to_search,)
        collects = self.collect_presenter.get_collect_page_presentation(collects, dto.page, dto.on_page, total)

        return SuccessResponse(collects)

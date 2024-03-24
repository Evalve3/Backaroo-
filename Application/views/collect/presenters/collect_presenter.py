from typing import List

from Application.views.collect.schemas import ShowCollectSchema, ShowCollectsSchema
from Application.views.user.schemas import UserPreviewSchema
from src.abc.collect.presenters.collect_presenter import ICollectPresenter
from src.dto.collects.collect import Collect


class CollectPresenter(ICollectPresenter):

    def get_collect_presentation(self, collect: Collect) -> ShowCollectSchema:
        author = UserPreviewSchema(
            uid=collect.author.uid,
            username=collect.author.username,
            avatar_file_id=collect.author.avatar_id,
            first_name=collect.author.first_name,
            last_name=collect.author.last_name,
        )

        return ShowCollectSchema(
            uid=collect.uid,
            name=collect.name,
            description=collect.description,
            target_amount=collect.target_amount,
            current_amount=collect.current_amount,
            category=collect.category.name,
            create_date=collect.create_date,
            status=collect.status,
            country=collect.country.name,
            image_file_id=collect.image_uid,
            author=author
        )

    def get_collect_page_presentation(self, collect_list: List[Collect],
                                      page: int, on_page: int, total: int) -> ShowCollectsSchema:
        collects = [self.get_collect_presentation(collect) for collect in collect_list]

        return ShowCollectsSchema(
            collects=collects,
            count=total,
            page=page,
            on_page=on_page
        )

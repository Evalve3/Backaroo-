from models.collect.collect_model import CollectModel
from src.dto.collects.collect import Collect
from src.dto.user.user import User
from src.dto.category.category import Country, CollectCategory


class CollectMapper:

    @staticmethod
    def to_dto(collect: CollectModel) -> Collect:
        country = Country(**collect.country.dict()) if collect.country else None
        author = User(**collect.author.dict()) if collect.author else None
        category = CollectCategory(**collect.category.dict()) if collect.category else None

        return Collect(
            name=collect.name,
            description=collect.description,
            target_amount=collect.target_amount,
            current_amount=collect.current_amount,
            category=category,
            create_date=collect.create_date,
            status=collect.status,
            country=country,
            image_uid=collect.image_id,
            author=author,
        )

    @staticmethod
    def to_model(collect: Collect) -> CollectModel:
        country_uid = collect.country.uid if collect.country else None
        author_uid = collect.author.uid if collect.author else None
        category_uid = collect.category.uid if collect.category else None

        return CollectModel(
            uid=collect.uid,
            name=collect.name,
            description=collect.description,
            target_amount=collect.target_amount,
            current_amount=collect.current_amount,
            category_id=category_uid,
            create_date=collect.create_date,
            status=collect.status,
            country_id=country_uid,
            image_id=collect.image_uid,
            author_id=author_uid
        )

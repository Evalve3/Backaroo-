from models.category.category_model import CollectCategoryModel
from src.dto.category.category import CollectCategory


class CategoryMapper:

    @staticmethod
    def to_dto(category: CollectCategoryModel) -> CollectCategory:
        category = CollectCategory(**category.dict())

        return category

    @staticmethod
    def to_model(country: CollectCategory) -> CollectCategoryModel:
        return CollectCategoryModel(
            uid=country.uid,
            name=country.name
        )

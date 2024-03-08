from models.category.country_model import CountryModel
from src.dto.category.category import Country


class CountryMapper:

    @staticmethod
    def to_dto(country: CountryModel) -> Country:
        country = Country(**country.dict())

        return country

    @staticmethod
    def to_model(country: Country) -> CountryModel:
        return CountryModel(
            uid=country.uid,
            name=country.name
        )

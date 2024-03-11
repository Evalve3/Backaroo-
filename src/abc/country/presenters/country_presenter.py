from abc import ABC, abstractmethod
from typing import List

from src.dto.category.category import Country


class ICountryPresenter(ABC):

    @abstractmethod
    def get_country_presentation(self, country: Country):
        pass

    @abstractmethod
    def get_country_list_presentation(self, country_list: List[Country]):
        pass

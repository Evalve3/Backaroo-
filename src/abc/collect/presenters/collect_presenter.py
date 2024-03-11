from abc import ABC, abstractmethod
from typing import List

from src.dto.collects.collect import Collect


class ICollectPresenter(ABC):

    @abstractmethod
    def get_collect_presentation(self, collect: Collect):
        pass

    @abstractmethod
    def get_collect_list_presentation(self, collect_list: List[Collect]):
        pass

    @abstractmethod
    def get_collect_page_presentation(self, collect_list: List[Collect], page: int, on_page: int, total: int):
        pass

    @abstractmethod
    def get_collect_preview_presentation(self, collect: Collect):
        pass

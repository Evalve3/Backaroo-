from abc import ABCMeta
from abc import abstractmethod

from typing import Any, Optional


class Response:
    def __init__(self, success: bool, data: Optional[Any] = None, error: Optional[str] = None):
        self.success = success
        self.data = data
        self.error = error


class BaseAsyncUseCase(metaclass=ABCMeta):
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Response:
        pass

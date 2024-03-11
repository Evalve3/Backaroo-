from abc import ABCMeta
from abc import abstractmethod

from typing import Any, Optional, Union


class Response:
    def __init__(self, code: int, data: Optional[Any] = None, error: Optional[str] = None):
        self.data = data
        self.code = code
        self.error = error

    def __str__(self):
        return f"Response(code={self.code}, data={self.data}, error={self.error})"


class SuccessResponse(Response):
    def __init__(self, data: Any, code: int = 200):
        super().__init__(code=code, data=data)


class ErrorResponse(Response):
    def __init__(self, error: str, code: int):
        super().__init__(code=code, error=error)


class BaseAsyncUseCase(metaclass=ABCMeta):
    @abstractmethod
    async def execute(self, *args, **kwargs) -> Union[SuccessResponse, ErrorResponse]:
        pass
